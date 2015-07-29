from django.contrib import admin
from inventoryapp.products.models import Products
from inventoryapp.reservations.admin import ReservationsInline
from inventoryapp.sales.admin import SalesInline


class ProductsAdmin(admin.ModelAdmin):
    inlines = [ReservationsInline, SalesInline]


admin.site.register(Products, ProductsAdmin)
