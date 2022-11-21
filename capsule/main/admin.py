from django.contrib import admin
from .models import Product, SizeCategory, TypeCategory, BrandCategory, Banner

admin.site.register(Product)
admin.site.register(SizeCategory)
admin.site.register(TypeCategory)
admin.site.register(BrandCategory)
admin.site.register(Banner)


