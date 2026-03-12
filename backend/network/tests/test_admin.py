import pytest
from django.contrib.admin.sites import AdminSite

from network.admin import NetworkNodeAdmin, clear_debt
from network.models import NetworkNode
from tests.factories import NetworkNodeFactory


pytestmark = pytest.mark.django_db


class MockRequest:
    pass


def test_clear_debt_admin_action():
    node1 = NetworkNodeFactory(debt="100.00")
    node2 = NetworkNodeFactory(debt="200.00")

    queryset = NetworkNode.objects.filter(id__in=[node1.id, node2.id])

    clear_debt(None, MockRequest(), queryset)

    node1.refresh_from_db()
    node2.refresh_from_db()

    assert node1.debt == 0
    assert node2.debt == 0