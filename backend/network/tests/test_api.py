import pytest

from tests.factories import SupplierFactory, NetworkNodeFactory


pytestmark = pytest.mark.django_db


def test_network_list(auth_client):
    NetworkNodeFactory.create_batch(3)

    response = auth_client.get("/api/network/")

    assert response.status_code == 200
    assert len(response.data) >= 3


def test_create_network_node(auth_client):
    supplier = SupplierFactory()

    data = {
        "name": "Retail Shop",
        "email": "retail@test.com",
        "country": "Germany",
        "city": "Berlin",
        "street": "Alexanderplatz",
        "house_number": "12",
        "supplier": supplier.id,
        "debt": "100.00",
    }

    response = auth_client.post("/api/network/", data, format="json")

    assert response.status_code == 201
    assert response.data["name"] == "Retail Shop"


def test_filter_network_by_country(auth_client):
    NetworkNodeFactory(country="USA")
    NetworkNodeFactory(country="Germany")

    response = auth_client.get("/api/network/?country=Germany")

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["country"] == "Germany"


def test_debt_is_not_updated_via_patch(auth_client):
    node = NetworkNodeFactory(debt="2500.00")

    response = auth_client.patch(
        f"/api/network/{node.id}/",
        {"debt": "9999.99"},
        format="json",
    )

    assert response.status_code == 200

    node.refresh_from_db()
    assert str(node.debt) == "2500.00"


def test_supplier_can_be_null_on_create(auth_client):
    data = {
        "name": "Factory",
        "email": "factory@test.com",
        "country": "USA",
        "city": "Detroit",
        "street": "Industrial Ave",
        "house_number": "1",
        "supplier": None,
        "debt": "0.00",
    }

    response = auth_client.post("/api/network/", data)

    assert response.status_code == 201
    assert response.data["supplier"] is None

def test_retrieve_network_node(auth_client):
    node = NetworkNodeFactory()

    response = auth_client.get(f"/api/network/{node.id}/")

    assert response.status_code == 200
    assert response.data["id"] == node.id


def test_update_network_node_fields(auth_client):
    node = NetworkNodeFactory(name="Old Name", city="Old City")

    response = auth_client.patch(
        f"/api/network/{node.id}/",
        {"name": "New Name", "city": "New City"},
        format="json",
    )

    assert response.status_code == 200

    node.refresh_from_db()
    assert node.name == "New Name"
    assert node.city == "New City"


def test_delete_network_node(auth_client):
    node = NetworkNodeFactory()

    response = auth_client.delete(f"/api/network/{node.id}/")

    assert response.status_code == 204