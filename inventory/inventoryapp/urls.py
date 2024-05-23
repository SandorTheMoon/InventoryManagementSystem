from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("addproduct/", views.addproduct_page, name="addproduct"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),
    
] 