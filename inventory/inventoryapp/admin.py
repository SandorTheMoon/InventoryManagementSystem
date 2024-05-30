from django.contrib import admin
from .models import Meats, Baked, Dairy, Plants, Condiments, Beverages, Dry, Packaging, NavBarCustomization, LoginCustomization, CompanyLogo

admin.site.register(Meats)
admin.site.register(Baked)
admin.site.register(Dairy)
admin.site.register(Plants)
admin.site.register(Condiments)
admin.site.register(Beverages)
admin.site.register(Dry)
admin.site.register(Packaging)

admin.site.register(NavBarCustomization)
admin.site.register(LoginCustomization)
admin.site.register(CompanyLogo)