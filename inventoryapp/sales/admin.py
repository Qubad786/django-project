from django.contrib import admin

from inventoryapp.sales.models import Sales


class SalesInline(admin.TabularInline):
    model = Sales
    extra = 1


class SalesAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_name', 'product_kind', 'units', 'sold_on', 'profit',)
    list_filter = ('user__email', 'product__name', 'units', 'sold_on', 'profit')
    search_fields = ('user__email', "user__username", 'product__name', "product__kind")

    # noinspection PyMethodMayBeStatic
    def product_kind(self, obj):
        return obj.product.kind

    # noinspection PyMethodMayBeStatic
    def product_name(self, obj):
        return obj.product.name


admin.site.register(Sales, SalesAdmin)

