from django.db import models
from network.models import NetworkNode


class Product(models.Model):

    name = models.CharField(max_length=255)

    model = models.CharField(max_length=255)

    release_date = models.DateField()

    network = models.ForeignKey(
        NetworkNode,
        related_name="products",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name