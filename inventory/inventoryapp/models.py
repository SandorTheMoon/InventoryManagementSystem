from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    unit_of_measurement = models.CharField(max_length=50)
    reorder_level = models.IntegerField()
    supplier = models.CharField(max_length=255)

    def __str__(self):
        return self.name

