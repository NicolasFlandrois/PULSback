from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(models.Model):
    company = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.company


class User(AbstractUser):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="users", null=True)
    is_admin = models.BooleanField(default=False)


class Campaign(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name="campaigns")
    name = models.CharField(max_length=255)
    description = models.TextField()
    html_template = models.TextField()

    def __str__(self):
        return self.name
