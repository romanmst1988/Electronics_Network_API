import pytest

from tests.factories import SupplierFactory, NetworkNodeFactory


pytestmark = pytest.mark.django_db


def test_network_node_str():
    node = NetworkNodeFactory(name="Retail Node")
    assert str(node) == "Retail Node"


def test_network_node_level_zero():
    supplier = SupplierFactory(supplier=None)
    assert supplier.level == 0


def test_network_node_level_one():
    factory = SupplierFactory(supplier=None)
    retail = NetworkNodeFactory(supplier=factory)
    assert retail.level == 1


def test_network_node_level_two():
    factory = SupplierFactory(supplier=None)
    retail = NetworkNodeFactory(supplier=factory)
    entrepreneur = NetworkNodeFactory(supplier=retail)
    assert entrepreneur.level == 2