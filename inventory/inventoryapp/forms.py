from django import forms
from .models import PurchaseOrder, CompanyLogo


class AddProductForm(forms.Form):
    CATEGORY_CHOICES = [
        ('Meats', 'Meats'),
        ('Baked', 'Bread & Baked Goods'),
        ('Dairy', 'Dairy Products'),
        ('Plants', 'Vegetable & Fruits'),
        ('Condiments', 'Condiments & Sauces'),
        ('Beverages', 'Beverages'),
        ('Dry', 'Dry Goods & Staples'),
        ('Packaging', 'Plastic/Paper & Packaging'),
    ]
    
    name = forms.CharField(max_length=255)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    description = forms.CharField(widget=forms.Textarea, required=False)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = forms.IntegerField()
    unit_of_measurement = forms.CharField(max_length=50)
    reorder_level = forms.IntegerField()
    supplier = forms.CharField(max_length=255)

class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ['company_name', 'company_address', 'supplier_name', 'supplier_address', 'order_status', 'name', 'description', 'quantity', 'unit_of_measurement', 'unit_price']

class PurchaseOrderStatusForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ['order_status']

class LogoForm(forms.ModelForm):
    class Meta:
        model = CompanyLogo
        fields = ['logo']