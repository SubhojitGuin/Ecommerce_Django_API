from django.db import models
from product.models import *
from decimal import Decimal
from django.core.validators import MinValueValidator

# Create your models here.
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pin_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    date_of_birth = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.first_name

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')
    
    def __str__(self):
        return self.user.first_name
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.JSONField()
    total_price = models.DecimalField(decimal_places=2, max_digits=10, default=0,
                                      validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        total = 0
        for product_id, quantity in self.cart.items():
            try:
                product = Product.objects.get(id=product_id)
                total += product.price * quantity
            except Product.DoesNotExist:
                continue
        self.total_price = total
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.user.first_name