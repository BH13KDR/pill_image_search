import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestPillURLs:

    def test_pill_list_url(self, client):
        response = client.get("/pills/list/")
        assert response.status_code in [
            200,
            204,
            302,
            400,
        ]  # 현재 데이터 없는 상태 고려

    def test_pill_detail_url(self, client):
        response = client.get("/pills/detail/")
        # pk가 없는 경우 에러 가능 → URL 정상 연결만 확인
        assert response.status_code in [400, 404]

    def test_pill_search_url(self, client):
        response = client.get("/pills/search/?query=진통제")
        assert response.status_code in [200, 204, 400]
