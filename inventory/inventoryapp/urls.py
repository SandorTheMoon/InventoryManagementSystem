from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("addproduct/", views.addproduct_page, name="addproduct"),
    path('update_product/<str:category>/<int:product_id>/', views.update_product, name='update_product'),
    path('delete_product/<str:category>/<int:product_id>/', views.delete_product, name='delete_product'),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),

    # === SUPPLIERS' URLS ===
    path("meats_list/", views.meats_list, name="meats_list"),

    # === UI CUSTOMIZATION URLS ===
    path("customization/", views.customization, name="customization"),
    path('customization/navigation/', views.navbar_customization, name='navbar_customization'),
    path('customization/save_navbar/', views.save_navbar_customization, name='save_navbar_customization'),
    path('customization/login/', views.login_customization, name='login_customization'),
    path('customization/save_login/', views.save_login_customization, name='save_login_customization'),
    
] 