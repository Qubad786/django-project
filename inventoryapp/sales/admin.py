from django.contrib import admin

from inventoryapp.sales.models import Sales


class SalesInline(admin.TabularInline):
    model = Sales
    extra = 1


class SalesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Sales, SalesAdmin)

