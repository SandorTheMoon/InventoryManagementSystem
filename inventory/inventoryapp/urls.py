from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("addproduct/", views.addproduct_page, name="addproduct"),
    path('update_product/<str:category>/<int:product_id>/', views.update_product, name='update_product'),
    path('delete_product/<str:category>/<int:product_id>/', views.delete_product, name='delete_product'),
    path('my_po/', views.my_po, name="my_po"),
    path('my_po_details/<int:pk>/', views.my_po_details, name="my_po_details"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),

    # === SUPPLIERS' URLS ===
    path("generate_po/", views.generate_po, name="generate_po"),
    path('my_generated_po/', views.my_generated_po, name='my_generated_po'),
    path('my_generated_po_details/<int:pk>/', views.my_generated_po_details, name='my_generated_po_details'),
    path("meats_list/", views.meats_list, name="meats_list"),
    path("baked_list/", views.baked_list, name="baked_list"),
    path("dairy_list/", views.dairy_list, name="dairy_list"),
    path("plants_list/", views.plants_list, name="plants_list"),
    path("condiments_list/", views.condiments_list, name="condiments_list"),
    path("beverages_list/", views.beverages_list, name="beverages_list"),
    path("dry_list/", views.dry_list, name="dry_list"),
    path("packaging_list/", views.packaging_list, name="packaging_list"),


    # === UI CUSTOMIZATION URLS ===
    path("customization/", views.customization, name="customization"),
    path('customization/navigation/', views.navbar_customization, name='navbar_customization'),
    path('customization/save_navbar/', views.save_navbar_customization, name='save_navbar_customization'),
    path('customization/login/', views.login_customization, name='login_customization'),
    path('customization/save_login/', views.save_login_customization, name='save_login_customization'),
    path('customization/mainpage/', views.mainpage_customization, name='mainpage_customization'),
    path('customization/mainpage/save_mainpage', views.save_mainpage_customization, name='save_mainpage_customization'),
] 