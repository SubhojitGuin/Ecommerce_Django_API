from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    quantity = models.PositiveIntegerField()
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image_path = models.TextField(max_length=1000 , null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


