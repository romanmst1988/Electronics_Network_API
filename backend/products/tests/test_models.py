import pytest
from tests.factories import ProductFactory

pytestmark = pytest.mark.django_db


def test_product_str():
    product = ProductFactory(name="iPhone", model="15 Pro")
    assert str(product) == "iPhone (15 Pro)"
