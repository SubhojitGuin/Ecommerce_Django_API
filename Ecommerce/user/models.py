from django.db import models

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

    