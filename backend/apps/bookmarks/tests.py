from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from apps.pills.models import PillItem
from apps.bookmarks.models import Bookmark

User = get_user_model()

class BookmarkAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="tester", email="test@example.com", password="pass1234"
        )
        self.client.login(username="tester", password="pass1234")
        self.pill = PillItem.objects.create(
            item_seq="101",
            item_name="테스트약",
            entp_name="테스트제약",
            item_image_url="http://example.com/test.jpg"
        )

    def test_add_bookmark(self):
        response = self.client.post("/bookmarks/", {"item_seq": "101"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["success"], True)
        self.assertEqual(response.data["message"], "약품이 북마크에 추가되었습니다.")
        self.assertEqual(response.data["current_count"], 1)

    def test_delete_bookmark(self):
        Bookmark.objects.create(user=self.user, pill=self.pill)
        response = self.client.delete("/bookmarks/101/")
        self.assert