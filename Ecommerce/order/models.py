from django.db import models
from user.models import *
from product.models import *
from django.core.validators import MinValueValidator

# Create your models here.
class Order(models.Model):
  order_id = models.AutoField(primary_key=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  cart = models.JSONField()
  total_price = models.DecimalField(decimal_places=2, max_digits=10, default=0,
                                      validators=[MinValueValidator(0)])
  order_date = models.DateTimeField(auto_now_add=True)
  paid = models.BooleanField(default=False)
  
  def __str__(self):
       return self.order_id