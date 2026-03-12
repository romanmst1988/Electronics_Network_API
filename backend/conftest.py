import pytest
from rest_framework.test import APIClient
from tests.factories import UserFactory


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def active_staff_user(db):
    return UserFactory()


@pytest.fixture
def inactive_user(db):
    return UserFactory(is_active=False)


@pytest.fixture
def non_staff_user(db):
    return UserFactory(is_staff=False)


@pytest.fixture
def auth_client(api_client, active_staff_user):
    api_client.force_authenticate(user=active_staff_user)
    return api_client
