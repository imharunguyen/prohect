from django.contrib import admin
from core.models import Customer, Category, Product

# Register your models here.

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)