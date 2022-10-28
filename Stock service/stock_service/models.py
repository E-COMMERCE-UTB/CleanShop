from email.policy import default
from random import choices
from django.db import models

CATEGORY_CHOICES = (
    ('L', 'Limpieza'),
    ('H', 'Hogar'),
    ('I', 'Industrial'),
)


class Product(models.Model):
    Name = models.CharField(max_length=700)
    Desc = models.TextField()
    Type = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    Quantity = models.PositiveIntegerField()
    Price = models.PositiveIntegerField()
    Provider_id = models.PositiveIntegerField()
    Product_pic = models.ImageField(blank=True, null=True)
    Active = models.BooleanField(default=False)
