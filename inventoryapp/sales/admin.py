from django.contrib import admin

from inventoryapp.sales.models import Sales


class SalesInline(admin.TabularInline):
    model = Sales
    classes = ('grp-collapse grp-closed',)
    extra = 1


class SalesAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'customer_address',
                    'product_name', 'product_kind', 'product_brand', 'units', 'sold_on', 'profit', )
    list_filter = ('user__email', 'product__name', 'units', 'sold_on', 'profit')
    search_fields = ('user__email', "user__username", 'product__name', "product__kind")

    fieldsets = (
        (
            'Edit Sales Record', {
                'classes': ('grp-collapse grp-open',),
                'fields': ('user', 'product', 'profit', 'units', 'sold_on'),
            }
        ),
    )

    raw_id_fields = ('user', 'product',)

    autocomplete_lookup_fields = {
        'fk': ['user', 'product'],
    }

    # noinspection PyMethodMayBeStatic
    def product_kind(self, sales):
        return sales.product.kind

    # noinspection PyMethodMayBeStatic
    def product_name(self, sales):
        return sales.product.name

    # noinspection PyMethodMayBeStatic
    def product_brand(self, sales):
        return sales.product.brand

    # noinspection PyMethodMayBeStatic
    def customer_name(self, sales):
        return sales.user.username

    # noinspection PyMethodMayBeStatic
    def customer_email(self, sales):
        return sales.user.email

    # noinspection PyMethodMayBeStatic
    def customer_address(self, sales):
        return sales.user.address


admin.site.register(Sales, SalesAdmin)

