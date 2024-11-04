from django.db import models
from order.models import Order
from django.core.validators import MinValueValidator

# Create your models here.
class Payment(models.Model):
    PAYMENT_STATUS = [
        ('success', 'Success'),
        ('failed', 'Failed')
    ]
    order = models.ForeignKey(Order, related_name='payments', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)])
    payment_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='failed')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Payment {self.payment_id} - {self.order.user.first_name}"
    
    class Meta:
        unique_together = ('order', 'payment_id')
