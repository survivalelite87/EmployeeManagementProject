from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Phone(models.Model):
    number = models.CharField(max_length=15)

    def __str__(self):
        return self.number
    
    def delete(self, *args, **kwargs):
        # Delete the associated Phone instance
        if self.phone:
            self.phone.delete()
        super().delete(*args, **kwargs)

class Employee(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)

    def __str__(self):
        return self.name