from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.PositiveIntegerField(help_text='Size unit (e.g., grams or ml or arbitrary unit)')
    category = models.CharField(max_length=100, blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.price}"
