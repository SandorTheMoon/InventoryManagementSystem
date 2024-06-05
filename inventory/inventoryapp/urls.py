from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home_page, name="home"),
    path("addproduct/", views.addproduct_page, name="addproduct"),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('my_po/', views.my_po, name="my_po"),
    path('my_po_details/<int:pk>/', views.my_po_details, name="my_po_details"),
    path("login/", views.login_page, name="login"),
    path("register/", views.registersupplier_page, name="register"),
    path("logout/", views.logout_page, name="logout"),

    # === SUPPLIERS' URLS ===
    path("generate_po/", views.generate_po, name="generate_po"),
    path('my_generated_po/', views.my_generated_po, name='my_generated_po'),
    path('my_generated_po_details/<int:pk>/', views.my_generated_po_details, name='my_generated_po_details'),
    path("products_list/", views.products_list, name="products_list"),

    # === UI CUSTOMIZATION URLS ===
    path("customization/", views.customization, name="customization"),
    path('customization/navigation/', views.navbar_customization, name='navbar_customization'),
    path('customization/save_navbar/', views.save_navbar_customization, name='save_navbar_customization'),
    path('customization/login/', views.login_customization, name='login_customization'),
    path('customization/save_login/', views.save_login_customization, name='save_login_customization'),
    path('customization/mainpage/', views.mainpage_customization, name='mainpage_customization'),
    path('customization/mainpage/save_mainpage', views.save_mainpage_customization, name='save_mainpage_customization'),
    path('customization/logo', views.logo_customization, name="logo_customization"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
