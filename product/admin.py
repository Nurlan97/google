from django.contrib import admin

# Register your models here.
from product.models import Product, NewProduct, Category

admin.site.register(Product)
admin.site.register(NewProduct)
admin.site.register(Category)