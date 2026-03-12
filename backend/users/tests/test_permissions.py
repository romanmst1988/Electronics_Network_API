import pytest
from tests.factories import NetworkNodeFactory

pytestmark = pytest.mark.django_db


def test_anonymous_user_has_no_access(api_client):
    NetworkNodeFactory()

    response = api_client.get("/api/network/")

    assert response.status_code in (401, 403)


def test_inactive_user_has_no_access(api_client, inactive_user):
    api_client.force_authenticate(user=inactive_user)

    response = api_client.get("/api/network/")

    assert response.status_code == 403


def test_non_staff_user_has_no_access(api_client, non_staff_user):
    api_client.force_authenticate(user=non_staff_user)

    response = api_client.get("/api/network/")

    assert response.status_code == 403
