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

class PurchaseOrder(models.Model):
    order_number = models.CharField(max_length=20, unique=True)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=255)
    supplier_name = models.CharField(max_length=100)
    supplier_address = models.CharField(max_length=255)
    order_status = models.CharField(
        max_length=20,
        choices=[
            ('PLACE_ORDER', 'Place Order'),
            ('TO_PROCESS', 'To Process'),
            ('TO_SHIP', 'To Ship'),
            ('TO_DELIVER', 'To Deliver'),
            ('DELIVERED', 'Delivered'),
            ('CANCEL_ORDER', 'Cancel Order'),
        ],
        null=True, blank=True
    )
    date_issued = models.DateField(auto_now_add=True)
    total_amount_payable = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchase_orders')
    name = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    unit_of_measurement = models.CharField(max_length=20, null=True, blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


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
