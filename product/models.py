from django.db import models
from django.utils import timezone

class ColorType(models.TextChoices):
    NONE = 'none', 'None'
    RED = 'red', 'Red'
    BLUE = 'blue', 'Blue'
    GREEN = 'green', 'Green'
        # Add more color choices as needed


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=20, choices=ColorType.choices, default=ColorType.NONE)
    weight = models.IntegerField()
    create_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


    def __str__(self) -> str:
        return self.name
