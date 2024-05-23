from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('Meats', 'Meats'),
        ('Bread & Baked Goods', 'Bread & Baked Goods'),
        ('Dairy Products', 'Dairy Products'),
        ('Vegetables & Fruits', 'Vegetables & Fruits'),
        ('Condiments & Sauces', 'Condiments & Sauces'),
        ('Beverages', 'Beverages'),
        ('Dry Goods & Staples', 'Dry Goods & Staples'),
        ('Plastic/Paper & Packaging', 'Plastic/Paper & Packaging'),
    ]
    
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'price', 'quantity_in_stock', 'unit_of_measurement', 'reorder_level', 'supplier']
