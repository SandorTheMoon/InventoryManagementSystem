from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import AddProductForm
from .models import Meats, Baked, Dairy, Plants, Condiments, Beverages, Dry, Packaging


def login_page(request):
    if request.user.is_authenticated:
        logout(request)
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

        return render(request, "authentication/login.html")


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

    return render(request, "home/homepage.html", {
        'meats_products': meats_products,
        'baked_products': baked_products,
        'dairy_products': dairy_products,
        'plants_products': plants_products,
        'condiments_products': condiments_products,
        'beverages_products': beverages_products,
        'dry_products': dry_products,
        'packaging_products': packaging_products,
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
    
    return render(request, "home/addproduct.html", {'form': form})


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

    return render(request, "home/update_product.html", {'form': form})


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

