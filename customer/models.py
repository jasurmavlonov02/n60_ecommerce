import uuid
import random

from django.db import models


def generate_vat_number():
    return str(random.randint(100_000_000, 999_999_999))


# Create your models here.

class Customer(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    joined = models.DateTimeField(auto_now_add=True)
    code = models.UUIDField(default=uuid.uuid4(), editable=False)
    vat_number = models.CharField(max_length=9, unique=True, default=generate_vat_number)
    image = models.ImageField(upload_to='customer/images/', blank=True, null=True)

    def __str__(self):
        return self.full_name
