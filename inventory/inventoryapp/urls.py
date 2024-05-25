from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("addproduct/", views.addproduct_page, name="addproduct"),
    path('update_product/<str:category>/<int:product_id>/', views.update_product, name='update_product'),
    path('delete_product/<str:category>/<int:product_id>/', views.delete_product, name='delete_product'),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),
    
] 