from django import forms



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