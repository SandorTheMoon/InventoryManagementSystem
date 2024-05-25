from django.db import models
from django.contrib.auth.models import User


class Meats(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default="Meats")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    unit_of_measurement = models.CharField(max_length=50)
    reorder_level = models.IntegerField()
    supplier = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Baked(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default="Bread & Baked Goods")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    unit_of_measurement = models.CharField(max_length=50)
    reorder_level = models.IntegerField()
    supplier = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Dairy(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default="Dairy Products")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    unit_of_measurement = models.CharField(max_length=50)
    reorder_level = models.IntegerField()
    supplier = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Plants(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default="Vegetable & Fruits")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    unit_of_measurement = models.CharField(max_length=50)
    reorder_level = models.IntegerField()
    supplier = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Condiments(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default="Condiments & Sauces")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    unit_of_measurement = models.CharField(max_length=50)
    reorder_level = models.IntegerField()
    supplier = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Beverages(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default="Beverages")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    unit_of_measurement = models.CharField(max_length=50)
    reorder_level = models.IntegerField()
    supplier = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Dry(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default="Dry Goods & Staples")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    unit_of_measurement = models.CharField(max_length=50)
    reorder_level = models.IntegerField()
    supplier = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Packaging(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default="Plastic/Paper & Packaging")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    unit_of_measurement = models.CharField(max_length=50)
    reorder_level = models.IntegerField()
    supplier = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# === MODELS FOR UI CUSTOMIZATIONS ===
class NavBarCustomization(models.Model):
    background_color = models.CharField(max_length=20, default='Blue')
    company_text_color = models.CharField(max_length=20, default='White')
    button_text_color = models.CharField(max_length=20, default='White')
    company_name = models.CharField(max_length=100, default='Company Name')

    def __str__(self):
        return 'NavBarCustomization'
    
class LoginCustomization(models.Model):
    background_color = models.CharField(max_length=20, default='White')
    box_color = models.CharField(max_length=20, default='white')
    title_text_color = models.CharField(max_length=20, default='Black')
    input_text_color = models.CharField(max_length=20, default='Black')
    button_color = models.CharField(max_length=20, default='Green')

    def __str__(self):
        return 'LoginCustomization'
