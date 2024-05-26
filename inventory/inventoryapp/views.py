from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse

import random
import string
from django.utils import timezone

from .forms import AddProductForm, PurchaseOrderForm, PurchaseOrderStatusForm
from .models import Meats, Baked, Dairy, Plants, Condiments, Beverages, Dry, Packaging, NavBarCustomization, LoginCustomization, MainPageCustomization, PurchaseOrder


def login_page(request):
    if request.user.is_authenticated:
        logout(user.request)
        return redirect('login')
    
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            
            else:
                messages.error(request, "Invalid login credentials!")

        customization = LoginCustomization.objects.first()
        if customization is None:
            customization = LoginCustomization.objects.create()

        return render(request, "authentication/login.html", {'customization': customization})


@login_required(login_url="/login/")
def logout_page(request):
    logout(request)
    return redirect("login")


@login_required(login_url="/login/")
def home_page(request):
    meats_products = Meats.objects.all()
    baked_products = Baked.objects.all()
    dairy_products = Dairy.objects.all()
    plants_products = Plants.objects.all()
    condiments_products = Condiments.objects.all()
    beverages_products = Beverages.objects.all()
    dry_products = Dry.objects.all()
    packaging_products = Packaging.objects.all()
    
    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()

    Mcustomization = MainPageCustomization.objects.first()
    if Mcustomization is None:
        Mcustomization = MainPageCustomization.objects.create()
    
    return render(request, "home/homepage.html", {
        'meats_products': meats_products,
        'baked_products': baked_products,
        'dairy_products': dairy_products,
        'plants_products': plants_products,
        'condiments_products': condiments_products,
        'beverages_products': beverages_products,
        'dry_products': dry_products,
        'packaging_products': packaging_products,

        'customization': customization,
        'Mcustomization': Mcustomization
    })


@login_required(login_url="/login/")
def addproduct_page(request):
    if request.method == "POST":
        form = AddProductForm(request.POST)

        if form.is_valid():
            category = form.cleaned_data['category']
            product_model = None

            if category == 'Meats':
                product_model = Meats
                using_dbs = ['default', 'meats_db']
            elif category == 'Baked':
                product_model = Baked
                using_dbs = ['default', 'baked_db']
            elif category == 'Dairy':
                product_model = Dairy
                using_dbs = ['default', 'dairy_db']
            elif category == 'Plants':
                product_model = Plants
                using_dbs = ['default', 'plants_db']
            elif category == 'Condiments':
                product_model = Condiments
                using_dbs = ['default', 'condiments_db']
            elif category == 'Beverages':
                product_model = Beverages
                using_dbs = ['default', 'beverages_db']
            elif category == 'Dry':
                product_model = Dry
                using_dbs = ['default', 'dry_db']
            elif category == 'Packaging':
                product_model = Packaging
                using_dbs = ['default', 'packaging_db']
            
            else:
                product_model = None
            
            if product_model:
                instance = product_model(**form.cleaned_data)
                for using_db in using_dbs:
                    instance._state.db = using_db
                    instance.save(using=using_db)
                
                messages.success(request, f"Product '{form.cleaned_data['name']}' added successfully!")
                return redirect('home')
    else:
        form = AddProductForm()
    
    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()

    Mcustomization = MainPageCustomization.objects.first()
    if Mcustomization is None:
        Mcustomization = MainPageCustomization.objects.create()
    
    return render(request, "home/addproduct.html", {'form': form, 'customization': customization, 'Mcustomization': Mcustomization})


@login_required(login_url="/login/")
def update_product(request, category, product_id):
    product_model = None
    if category == 'Meats':
        product_model = Meats
        using_db = 'meats_db'
    elif category == 'Baked':
        product_model = Baked
        using_db = 'baked_db'
    elif category == 'Dairy':
        product_model = Dairy
        using_db = 'dairy_db'
    elif category == 'Plants':
        product_model = Plants
        using_db = 'plants_db'
    elif category == 'Condiments':
        product_model = Condiments
        using_db = 'condiments_db'
    elif category == 'Beverages':
        product_model = Beverages
        using_db = 'beverages_db'
    elif category == 'Dry':
        product_model = Dry
        using_db = 'dry_db'
    elif category == 'Packaging':
        product_model = Packaging
        using_db = 'packaging_db'

    if not product_model:
        messages.error(request, "Invalid product category")
        return redirect('home')

    product = get_object_or_404(product_model, id=product_id)

    if request.method == "POST":
        form = AddProductForm(request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.quantity_in_stock = form.cleaned_data['quantity_in_stock']
            product.unit_of_measurement = form.cleaned_data['unit_of_measurement']
            product.reorder_level = form.cleaned_data['reorder_level']
            product.supplier = form.cleaned_data['supplier']
            product.save(using='default')
            product.save(using=using_db)
            messages.success(request, f"Product '{product.name}' updated successfully!")
            return redirect('home')
    else:
        form = AddProductForm(initial={
            'category': category,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'quantity_in_stock': product.quantity_in_stock,
            'unit_of_measurement': product.unit_of_measurement,
            'reorder_level': product.reorder_level,
            'supplier': product.supplier
        })

    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()

    return render(request, "home/update_product.html", {'form': form, 'customization': customization})


@login_required(login_url="/login/")
def delete_product(request, category, product_id):
    print("Category:", category)
    print("Product ID:", product_id)

    product_model = None
    if category == 'Meats':
        product_model = Meats
        using_db = 'meats_db'
    elif category == 'Baked':
        product_model = Baked
        using_db = 'baked_db'
    elif category == 'Dairy':
        product_model = Dairy
        using_db = 'dairy_db'
    elif category == 'Plants':
        product_model = Plants
        using_db = 'plants_db'
    elif category == 'Condiments':
        product_model = Condiments
        using_db = 'condiments_db'
    elif category == 'Beverages':
        product_model = Beverages
        using_db = 'beverages_db'
    elif category == 'Dry':
        product_model = Dry
        using_db = 'dry_db'
    elif category == 'Packaging':
        product_model = Packaging
        using_db = 'packaging_db'

    print("Product Model:", product_model)

    if not product_model:
        messages.error(request, "Invalid product category")
        return redirect('home')

    product = get_object_or_404(product_model, id=product_id)
    product1 = get_object_or_404(product_model, id=product_id)
    print("Product:", product)
    
    product.delete(using=using_db)
    product1.delete(using='default')
    messages.success(request, f"Product '{product.name}' deleted successfully!")
    return redirect('home')


@login_required(login_url="/login/")
def my_po(request):
    purchase_orders = PurchaseOrder.objects.all()

    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()

    return render(request, "home/my_po.html", {'purchase_orders': purchase_orders, 'customization': customization})


@login_required(login_url="/login/")
def my_po_details(request, pk):
    purchase_order = get_object_or_404(PurchaseOrder, pk=pk)
    if request.method == 'POST':
        form = PurchaseOrderStatusForm(request.POST, instance=purchase_order)
        if form.is_valid():
            form.save()
            return redirect('my_po')
    else:
        form = PurchaseOrderStatusForm(instance=purchase_order)

    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()
    
    return render(request, 'home/my_po_details.html', {'purchase_order': purchase_order, 'form': form, 'customization': customization})


# === FOR SUPPLIERS ===
from django.db import connections

def generate_order_number():
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    order_number = f'{timestamp}-{random_string}'
    return order_number

@login_required(login_url="/login/")
def generate_po(request):
    if request.method == "POST":
        form = PurchaseOrderForm(request.POST)
        if form.is_valid():
            purchase_order = form.save(commit=False)
            purchase_order.created_by = request.user
            get_username = request.user.username

            if get_username == 'meat':
                purchase_order.category = "Meats"

            elif get_username == 'baked':
                purchase_order.category = "Bread & Baked Goods"

            elif get_username == 'dairy':
                purchase_order.category = "Dairy Products"

            elif get_username == 'plants':
                purchase_order.category = "Vegetable & Fruits"

            elif get_username == 'condiments':
                purchase_order.category = "Condiments & Sauces"

            elif get_username == 'beverages':
                purchase_order.category = "Beverages"

            elif get_username == 'dry':
                purchase_order.category = "Dry Goods & Staples"

            elif get_username == 'packaging':
                purchase_order.category = "Plastic/Paper & Packaging"

            else:
                purchase_order.category = "Unknown"

            purchase_order.order_number = generate_order_number()  # Generate unique order number

            purchase_order.total_amount_payable = purchase_order.quantity * purchase_order.unit_price
            purchase_order.save()
            messages.success(request, "Purchase order created successfully!")
            return redirect('home')
        else:
            messages.error(request, "Failed to create purchase order. Please check the form.")
    else:
        form = PurchaseOrderForm()

    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()
    
    return render(request, "purchaseorders/generate_po.html", {'form': form, 'customization': customization})


@login_required(login_url="/login/")
def my_generated_po(request):
    purchase_orders = PurchaseOrder.objects.filter(created_by=request.user)

    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()

    return render(request, "purchaseorders/my_generated_po.html", {'purchase_orders': purchase_orders, 'customization': customization})


@login_required(login_url="/login/")
def my_generated_po_details(request, pk):
    purchase_order = get_object_or_404(PurchaseOrder, pk=pk)
    if request.method == 'POST':
        form = PurchaseOrderStatusForm(request.POST, instance=purchase_order)
        if form.is_valid():
            form.save()
            return redirect('my_generated_po')
    else:
        form = PurchaseOrderStatusForm(instance=purchase_order)

    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()
    
    return render(request, 'purchaseorders/my_generated_po_details.html', {'purchase_order': purchase_order, 'form': form, 'customization': customization})


@login_required(login_url="/login/")
def meats_list(request):
    with connections['meats_db'].cursor() as cursor:
        cursor.execute("""
            SELECT id, name, category, description, price, quantity_in_stock,
                   unit_of_measurement, reorder_level, supplier 
            FROM inventoryapp_meats;
        """)
        meats = cursor.fetchall()
    
    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()

    return render(request, 'suppliers/meats_list.html', {'meats': meats, 'customization': customization})


@login_required(login_url="/login/")
def baked_list(request):
    with connections['baked_db'].cursor() as cursor:
        cursor.execute("""
            SELECT id, name, category, description, price, quantity_in_stock,
                   unit_of_measurement, reorder_level, supplier 
            FROM inventoryapp_baked;
        """)
        baked = cursor.fetchall()
    
    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()

    return render(request, 'suppliers/baked_list.html', {'baked': baked, 'customization': customization})


@login_required(login_url="/login/")
def dairy_list(request):
    with connections['dairy_db'].cursor() as cursor:
        cursor.execute("""
            SELECT id, name, category, description, price, quantity_in_stock,
                   unit_of_measurement, reorder_level, supplier 
            FROM inventoryapp_dairy;
        """)
        dairy = cursor.fetchall()
    
    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()

    return render(request, 'suppliers/dairy_list.html', {'dairy': dairy, 'customization': customization})


@login_required(login_url="/login/")
def plants_list(request):
    with connections['plants_db'].cursor() as cursor:
        cursor.execute("""
            SELECT id, name, category, description, price, quantity_in_stock,
                   unit_of_measurement, reorder_level, supplier 
            FROM inventoryapp_plants;
        """)
        plants = cursor.fetchall()
    
    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()

    return render(request, 'suppliers/plants_list.html', {'plants': plants, 'customization': customization})


@login_required(login_url="/login/")
def condiments_list(request):
    with connections['condiments_db'].cursor() as cursor:
        cursor.execute("""
            SELECT id, name, category, description, price, quantity_in_stock,
                   unit_of_measurement, reorder_level, supplier 
            FROM inventoryapp_condiments;
        """)
        condiments = cursor.fetchall()
    
    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()

    return render(request, 'suppliers/condiments_list.html', {'condiments': condiments, 'customization': customization})


@login_required(login_url="/login/")
def beverages_list(request):
    with connections['beverages_db'].cursor() as cursor:
        cursor.execute("""
            SELECT id, name, category, description, price, quantity_in_stock,
                   unit_of_measurement, reorder_level, supplier 
            FROM inventoryapp_beverages;
        """)
        beverages = cursor.fetchall()
    
    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()

    return render(request, 'suppliers/beverages_list.html', {'beverages': beverages, 'customization': customization})


@login_required(login_url="/login/")
def dry_list(request):
    with connections['dry_db'].cursor() as cursor:
        cursor.execute("""
            SELECT id, name, category, description, price, quantity_in_stock,
                   unit_of_measurement, reorder_level, supplier 
            FROM inventoryapp_dry;
        """)
        dry = cursor.fetchall()
    
    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()

    return render(request, 'suppliers/dry_list.html', {'dry': dry, 'customization': customization})


@login_required(login_url="/login/")
def packaging_list(request):
    with connections['packaging_db'].cursor() as cursor:
        cursor.execute("""
            SELECT id, name, category, description, price, quantity_in_stock,
                   unit_of_measurement, reorder_level, supplier 
            FROM inventoryapp_packaging;
        """)
        packaging = cursor.fetchall()
    
    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()

    return render(request, 'suppliers/packaging_list.html', {'packaging': packaging, 'customization': customization})


# === FOR CUSTOMIZING UI ===
def customization(request):
    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()

    Mcustomization = MainPageCustomization.objects.first()
    if Mcustomization is None:
        Mcustomization = MainPageCustomization.objects.create()

    return render(request, "customization/customization.html", {'customization': customization, 'Mcustomization': Mcustomization})


def navbar_customization(request):
    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()
    
    return render(request, 'customization/navbar_customization.html', {'customization': customization})


def save_navbar_customization(request):
    if request.method == "POST":
        background_color = request.POST.get('background_color')
        company_text_color = request.POST.get('company_text_color')
        button_text_color = request.POST.get('button_text_color')
        company_name = request.POST.get('company_name')

        customization = NavBarCustomization.objects.first()
        if customization is None:
            customization = NavBarCustomization.objects.create()

        customization.background_color = background_color
        customization.company_text_color = company_text_color
        customization.button_text_color = button_text_color
        customization.company_name = company_name
        customization.save()

    return redirect('customization')


def login_customization(request):
    Lcustomization = LoginCustomization.objects.first()
    if Lcustomization is None:
        Lcustomization = LoginCustomization.objects.create()

    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()
    
    return render(request, 'customization/login_customization.html', {'Lcustomization': Lcustomization, 'customization': customization})


def save_login_customization(request):
    if request.method == "POST":
        background_color = request.POST.get('background_color')
        box_color = request.POST.get('box_color')
        title_text_color = request.POST.get('title_text_color')
        input_text_color = request.POST.get('input_text_color')
        button_color = request.POST.get('button_color')

        Lcustomization = LoginCustomization.objects.first()
        if Lcustomization is None:
            Lcustomization = LoginCustomization.objects.create()

        Lcustomization.background_color = background_color
        Lcustomization.box_color = box_color
        Lcustomization.title_text_color = title_text_color
        Lcustomization.input_text_color = input_text_color
        Lcustomization.button_color = button_color
        Lcustomization.save()

    return redirect('login_customization')


def mainpage_customization(request):
    Mcustomization = MainPageCustomization.objects.first()
    if Mcustomization is None:
        Mcustomization = MainPageCustomization.objects.create()

    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()
    
    return render(request, 'customization/mainpage_customization.html', {'Mcustomization': Mcustomization, 'customization': customization})

def save_mainpage_customization(request):
    if request.method == "POST":
        background_color = request.POST.get('background_color')
        box_color = request.POST.get('box_color')
        title_text_color = request.POST.get('title_text_color')
        table_header_text_color = request.POST.get('table_header_text_color')
        table_header_color = request.POST.get('table_header_color')
        table_text_color = request.POST.get('table_text_color')
        table_row_color = request.POST.get('table_row_color')

        Mcustomization = MainPageCustomization.objects.first()
        if Mcustomization is None:
            Mcustomization = MainPageCustomization.objects.create()

        Mcustomization.background_color = background_color
        Mcustomization.box_color = box_color
        Mcustomization.title_text_color = title_text_color
        Mcustomization.table_header_text_color = table_header_text_color
        Mcustomization.table_header_color = table_header_color
        Mcustomization.table_text_color = table_text_color
        Mcustomization.table_row_color = table_row_color
        Mcustomization.save()

    return redirect('mainpage_customization')
