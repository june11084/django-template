from django.db import models

# Create your models here.
PRODUCT_CATEGORY = (
    ('Electronic', 'Electronic'),
    ('Dairy', 'Dairy'),
    ('Snack', 'Snack'),
    ('Other', 'Other'),
)


class Product(models.Model):
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()
    category = models.CharField(max_length=20, blank=True, choices=PRODUCT_CATEGORY)

    def __str__(self):
        return self.description
