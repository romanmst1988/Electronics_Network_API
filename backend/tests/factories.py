import factory
from django.contrib.auth import get_user_model
from network.models import NetworkNode
from products.models import Product

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        skip_postgeneration_save = True

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@test.com")
    is_active = True
    is_staff = True

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        password = extracted or "testpass123"
        self.set_password(password)
        if create:
            self.save()


class SupplierFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = NetworkNode

    name = factory.Sequence(lambda n: f"Supplier {n}")
    email = factory.Sequence(lambda n: f"supplier{n}@test.com")
    country = "USA"
    city = "New York"
    street = "Main street"
    house_number = "1"
    supplier = None
    debt = "0.00"


class NetworkNodeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = NetworkNode

    name = factory.Sequence(lambda n: f"Node {n}")
    email = factory.Sequence(lambda n: f"node{n}@test.com")
    country = "USA"
    city = "Boston"
    street = "Second street"
    house_number = "10"
    supplier = factory.SubFactory(SupplierFactory)
    debt = "1500.50"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: f"Product {n}")
    model = factory.Sequence(lambda n: f"Model-{n}")
    release_date = "2024-01-01"
    network = factory.SubFactory(NetworkNodeFactory)
