from django.db import models
from django.contrib.auth.models import User

# === SUPPLIER PROFILE ===
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    is_supplier = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


# === PRODUCT DATABASE ===
class Products(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default="None")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    unit_of_measurement = models.CharField(max_length=50)
    reorder_level = models.IntegerField()
    expiration_date = models.DateField(null=True, blank=True)
    supplier = models.ForeignKey(UserProfile, on_delete=models.CASCADE, limit_choices_to={'is_supplier': True})
    
    def __str__(self):
        return self.name
    

# === PURCHASE ORDERS ===
class PurchaseOrder(models.Model):
    order_number = models.CharField(max_length=20, unique=True)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=255)
    supplier_name = models.CharField(max_length=100)
    supplier_address = models.CharField(max_length=255)
    order_status = models.CharField(
        max_length=20,
        choices=[
            ('PENDING', 'Pending'),
            ('ACCEPTED', 'Accept'),
            ('REJECTED', 'Reject'),
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
        return 'NavBar Customization'
    
class LoginCustomization(models.Model):
    background_color = models.CharField(max_length=20, default='White')
    box_color = models.CharField(max_length=20, default='white')
    title_text_color = models.CharField(max_length=20, default='Black')
    input_text_color = models.CharField(max_length=20, default='Black')
    button_color = models.CharField(max_length=20, default='Green')

    def __str__(self):
        return 'Login Customization'

class MainPageCustomization(models.Model):
    background_color = models.CharField(max_length=20, default='White')
    box_color = models.CharField(max_length=20, default='white')
    title_text_color = models.CharField(max_length=20, default='Black')
    table_header_text_color = models.CharField(max_length=20, default='Black')
    table_header_color = models.CharField(max_length=20, default='#f4f4f4')
    table_text_color = models.CharField(max_length=20, default='Black')
    table_row_color = models.CharField(max_length=20, default='#fff')

    def __str__(self):
        return 'Main Page Customization'
    
class CompanyLogo(models.Model):
    logo = models.ImageField(upload_to="logo/", null=True, blank=True)

    def __str__(self):
        return 'Image Logo'