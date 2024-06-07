from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, PurchaseOrder, CompanyLogo


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username', required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    company_name = forms.CharField(max_length=100, label='Company Name', required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'company_name']

class SupplierModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.company_name

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
    expiration_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))
    supplier = SupplierModelChoiceField(queryset=UserProfile.objects.filter(is_supplier=True))

class PurchaseOrderForm(forms.ModelForm):
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

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=False)

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