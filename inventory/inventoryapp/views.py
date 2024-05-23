from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import ProductForm
from .models import Product

# Create your views here.

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
    products_by_category = {}
    products = Product.objects.all()

    for product in products:
        if product.category in products_by_category:
            products_by_category[product.category].append(product)
            
        else:
            products_by_category[product.category] = [product]

    return render(request, "home/homepage.html", {'products_by_category': products_by_category})


@login_required(login_url="/login/")
def addproduct_page(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Form is not valid!')
    else:
        form = ProductForm()
    return render(request, "home/addproduct.html", {'form': form})