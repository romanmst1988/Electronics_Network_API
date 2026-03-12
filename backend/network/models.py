from django.db import models


class NetworkNode(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=20)

    supplier = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="clients",
        verbose_name="Поставщик",
    )

    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Задолженность перед поставщиком",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"

    def __str__(self):
        return self.name

    @property
    def level(self):
        level = 0
        supplier = self.supplier
        while supplier:
            level += 1
            supplier = supplier.supplier
        return level