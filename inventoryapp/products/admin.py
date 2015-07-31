from django.contrib import admin
from inventoryapp.products.models import Products
from inventoryapp.reservations.admin import ReservationsInline
from inventoryapp.sales.admin import SalesInline


class ProductsAdmin(admin.ModelAdmin):
    inlines = [ReservationsInline, SalesInline]
    list_display = ('name', 'kind', 'brand', 'units', 'actual_unit_price', 'added_on')
    list_filter = ('name', 'kind', 'brand', 'added_on', 'actual_unit_price')
    search_fields = ('name', 'kind', 'brand')

admin.site.register(Products, ProductsAdmin)
