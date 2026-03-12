import pytest
from tests.factories import UserFactory

pytestmark = pytest.mark.django_db


def test_jwt_token_obtain(api_client):
    user = UserFactory(username="adminuser", password="strongpass123")

    response = api_client.post(
        "/api/token/",
        {
            "username": "adminuser",
            "password": "strongpass123",
        },
        format="json",
    )

    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data
