from django.contrib import admin
from .models import UserProfile, Products, PurchaseOrder, NavBarCustomization, LoginCustomization, CompanyLogo

admin.site.register(UserProfile)

admin.site.register(Products)
admin.site.register(PurchaseOrder)

admin.site.register(NavBarCustomization)
admin.site.register(LoginCustomization)
admin.site.register(CompanyLogo)