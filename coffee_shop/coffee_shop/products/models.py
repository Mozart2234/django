from django.db import models


class Product(models.Model):
    name = models.TextField(max_length=255, verbose_name="Product Name")
    description = models.TextField(max_length=300, verbose_name="Product Description")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Product Price"
    )
    available = models.BooleanField(default=True, verbose_name="Product Availability")
    photo = models.ImageField(
        upload_to="products", null=True, blank=True, verbose_name="Product Photo"
    )

    def __str__(self):
        return f"{self.name}"
