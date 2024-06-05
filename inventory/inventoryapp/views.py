from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

import random
import string
from django.utils import timezone

from .forms import UserRegistrationForm, AddProductForm, PurchaseOrderForm, PurchaseOrderStatusForm, LogoForm
from .models import UserProfile, Products, NavBarCustomization, LoginCustomization, MainPageCustomization, CompanyLogo, PurchaseOrder

def registersupplier_page(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            company_name = form.cleaned_data['company_name']
            user = User.objects.create_user(username=username, password=password)
            profile = UserProfile(user=user, company_name=company_name)
            profile.save()
            return redirect('meats_list')
        
    else:
        form = UserRegistrationForm()

    CLcustomization, created = CompanyLogo.objects.get_or_create()

    if CLcustomization is None:
        CLcustomization = CompanyLogo.objects.create()

    customization = LoginCustomization.objects.first()
    if customization is None:
        customization = LoginCustomization.objects.create()

    return render(request, 'authentication/register.html', {'form': form, 'CLcustomization': CLcustomization, 'customization': customization})


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

        CLcustomization, created = CompanyLogo.objects.get_or_create()

        if CLcustomization is None:
            CLcustomization = CompanyLogo.objects.create()

        customization = LoginCustomization.objects.first()
        if customization is None:
            customization = LoginCustomization.objects.create()

        return render(request, "authentication/login.html", {'CLcustomization': CLcustomization, 'customization': customization})


@login_required(login_url="/login/")
def logout_page(request):
    logout(request)
    return redirect("login")


@login_required(login_url="/login/")
def home_page(request):
    products = Products.objects.all()

    CLcustomization = CompanyLogo.objects.first()
    if CLcustomization is None:
        CLcustomization = CompanyLogo.objects.create()

    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()

    Mcustomization = MainPageCustomization.objects.first()
    if Mcustomization is None:
        Mcustomization = MainPageCustomization.objects.create()

    PO = PurchaseOrder.objects.filter(order_status=None)
    countPO = PO.count()
    
    return render(request, "home/homepage.html", {
        'products': products,

        'CLcustomization': CLcustomization, 
        'customization': customization,
        'Mcustomization': Mcustomization,
        'countPO': countPO
    })


@login_required(login_url="/login/")
def addproduct_page(request):
    if request.method == "POST":
        form = AddProductForm(request.POST)
        if form.is_valid():
            Products.objects.create(**form.cleaned_data)
            return redirect('home')  
    else:
        form = AddProductForm()

    CLcustomization = CompanyLogo.objects.first() or CompanyLogo.objects.create()
    customization = NavBarCustomization.objects.first() or NavBarCustomization.objects.create()
    Mcustomization = MainPageCustomization.objects.first() or MainPageCustomization.objects.create()
    
    return render(request, "home/addproduct.html", {'CLcustomization': CLcustomization, 'form': form, 'customization': customization, 'Mcustomization': Mcustomization})


@login_required(login_url="/login/")
def update_product(request, product_id):
    product = get_object_or_404(Products, pk=product_id)

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
            product.save()
            return redirect('home')
    else:
        form = AddProductForm(initial={
            'name': product.name,
            'category': product.category,
            'description': product.description,
            'price': product.price,
            'quantity_in_stock': product.quantity_in_stock,
            'unit_of_measurement': product.unit_of_measurement,
            'reorder_level': product.reorder_level,
            'supplier': product.supplier
        })

    CLcustomization = CompanyLogo.objects.first() or CompanyLogo.objects.create()
    customization = NavBarCustomization.objects.first() or NavBarCustomization.objects.create()

    return render(request, "home/update_product.html", {'CLcustomization': CLcustomization, 'form': form, 'customization': customization})


@login_required(login_url="/login/")
def delete_product(request, product_id):
    product = get_object_or_404(Products, pk=product_id)

    product.delete()
    return redirect('home')



@login_required(login_url="/login/")
def my_po(request):
    purchase_orders = PurchaseOrder.objects.all().order_by('-date_issued')

    CLcustomization = CompanyLogo.objects.first()

    if CLcustomization is None:
        CLcustomization = CompanyLogo.objects.create()

    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()

    return render(request, "home/my_po.html", {'CLcustomization': CLcustomization, 'purchase_orders': purchase_orders, 'customization': customization})


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

    CLcustomization = CompanyLogo.objects.first()

    if CLcustomization is None:
        CLcustomization = CompanyLogo.objects.create()

    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()
    
    return render(request, 'home/my_po_details.html', {'CLcustomization': CLcustomization, 'purchase_order': purchase_order, 'form': form, 'customization': customization})


# === FOR SUPPLIERS ===
from django.db import connections

def generate_order_number():
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    order_number = f'{timestamp}-{random_string}'
    return order_number

@login_required(login_url="/login/")
def generate_po(request):
    if request.method == 'POST':
        form = PurchaseOrderForm(request.POST)
        if form.is_valid():
            purchase_order = form.save(commit=False)
            purchase_order.created_by = request.user
            purchase_order.order_number = generate_order_number()

            purchase_order.total_amount_payable = purchase_order.quantity * purchase_order.unit_price
            purchase_order.save()
            return redirect('products_list')
        else:
            for field, errors in form.errors.items():
                print(f"Error in field '{field}': {', '.join(errors)}")
    else:
        form = PurchaseOrderForm()

    CLcustomization = CompanyLogo.objects.first()
    if CLcustomization is None:
        CLcustomization = CompanyLogo.objects.create()

    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()
    
    return render(request, "purchaseorders/generate_po.html", {'CLcustomization': CLcustomization, 'customization': customization, 'form': form})


@login_required(login_url="/login/")
def my_generated_po(request):
    purchase_orders = PurchaseOrder.objects.filter(created_by=request.user).order_by('-date_issued') 

    CLcustomization = CompanyLogo.objects.first()

    if CLcustomization is None:
        CLcustomization = CompanyLogo.objects.create()

    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()

    return render(request, "purchaseorders/my_generated_po.html", {'CLcustomization': CLcustomization, 'purchase_orders': purchase_orders, 'customization': customization})


@login_required(login_url="/login/")
def my_generated_po_details(request, pk):
    purchase_order = get_object_or_404(PurchaseOrder, pk=pk)

    CLcustomization = CompanyLogo.objects.first()

    if CLcustomization is None:
        CLcustomization = CompanyLogo.objects.create()

    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()
    
    return render(request, 'purchaseorders/my_generated_po_details.html', {'CLcustomization': CLcustomization, 'purchase_order': purchase_order, 'customization': customization})


@login_required(login_url="/login/")
def products_list(request):
    supplier_profile = request.user.userprofile
    products = Products.objects.filter(supplier=supplier_profile)

    CLcustomization = CompanyLogo.objects.first()
    if CLcustomization is None:
        CLcustomization = CompanyLogo.objects.create()

    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()

    return render(request, 'suppliers/products_list.html', {'CLcustomization': CLcustomization, 'customization': customization, 'products': products})

# === FOR CUSTOMIZING UI ===
def customization(request):
    CLcustomization = CompanyLogo.objects.first()

    if CLcustomization is None:
        CLcustomization = CompanyLogo.objects.create()

    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()

    Mcustomization = MainPageCustomization.objects.first()
    if Mcustomization is None:
        Mcustomization = MainPageCustomization.objects.create()

    return render(request, "customization/customization.html", {'CLcustomization': CLcustomization, 'customization': customization, 'Mcustomization': Mcustomization})


def navbar_customization(request):
    CLcustomization = CompanyLogo.objects.first()

    if CLcustomization is None:
        CLcustomization = CompanyLogo.objects.create()

    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()
    
    return render(request, 'customization/navbar_customization.html', {'CLcustomization': CLcustomization, 'customization': customization})


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
    CLcustomization = CompanyLogo.objects.first()

    if CLcustomization is None:
        CLcustomization = CompanyLogo.objects.create()

    Lcustomization = LoginCustomization.objects.first()
    if Lcustomization is None:
        Lcustomization = LoginCustomization.objects.create()

    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()
    
    return render(request, 'customization/login_customization.html', {'CLcustomization': CLcustomization, 'Lcustomization': Lcustomization, 'customization': customization})


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
    CLcustomization = CompanyLogo.objects.first()

    if CLcustomization is None:
        CLcustomization = CompanyLogo.objects.create()

    Mcustomization = MainPageCustomization.objects.first()
    if Mcustomization is None:
        Mcustomization = MainPageCustomization.objects.create()

    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()
    
    return render(request, 'customization/mainpage_customization.html', {'CLcustomization': CLcustomization, 'Mcustomization': Mcustomization, 'customization': customization})

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


@login_required(login_url="/login/")
def logo_customization(request):
    CLcustomization = CompanyLogo.objects.first()

    if CLcustomization is None:
        CLcustomization = CompanyLogo.objects.create()

    customization = NavBarCustomization.objects.first()
    if customization is None:
        customization = NavBarCustomization.objects.create()

    if request.method == "POST":
        form = LogoForm(request.POST, request.FILES, instance=CLcustomization)

        if form.is_valid():
            form.save()
            return redirect('logo_customization')
        
    else:
            form = LogoForm(instance=CLcustomization)

    return render(request, 'customization/logo_customization.html', {'CLcustomization': CLcustomization, 'customization': customization, 'form': form})