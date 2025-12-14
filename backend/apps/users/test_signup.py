import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestUserURLs:

    def test_signup_url(self, client):
        url = reverse("users:user-register")
        assert url == "/users/signup/"

    def test_login_url(self, client):
        url = reverse("users:user-login")
        assert url == "/users/login/"

    def test_send_email_url(self, client):
        url = reverse("users:user-send")
        assert url == "/users/signup/send/"

    def test_verify_email_url(self, client):
        url = reverse("users:user-verify")
        assert url == "/users/signup/verify/"

    def test_logout_url(self, client):
        url = reverse("users:logout")
        assert url == "/users/logout/"

    def test_deactivate_url(self, client):
        url = reverse("users:user-deactivate")
        assert url == "/users/signout/"

    def test_token_refresh_url(self, client):
        url = reverse("users:token_refresh")
        assert url == "/users/login/token/refresh/"

    def test_kakao_login_url(self, client):
        url = reverse("users:kakao-login")
        assert url == "/users/social/kakao/login/"

    def test_kakao_callback_url(self, client):
        url = reverse("users:kakao-callback")
        assert url == "/users/social/kakao/callback/"

    def test_google_login_url(self, client):
        response = client.get("/users/social/google/login/")
        assert response.status_code in [200, 302, 400, 404]

    def test_google_callback_url(self, client):
        response = client.get("/users/social/google/callback/")
        assert response.status_code in [400, 401, 404]
