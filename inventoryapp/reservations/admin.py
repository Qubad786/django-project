from django.contrib import admin

from inventoryapp.reservations.models import Reservations


class ReservationsInline(admin.TabularInline):
    model = Reservations
    classes = ('grp-collapse grp-closed',)
    extra = 1


class ReservationsAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'customer_address', 'product_name', 'product_kind',
                    'product_brand', 'ordered_units', 'ordered_on', 'price',)
    list_filter = ('user__email', 'product__name', 'ordered_units', 'ordered_on', 'price')
    search_fields = ('user__email', "user__username", 'product__name', "product__kind")

    fieldsets = (
        (
            'Edit Orders Record', {
                'classes': ('grp-collapse grp-open',),
                'fields': ('user', 'product', 'price', 'ordered_units', 'ordered_on'),
            }
        ),
    )

    raw_id_fields = ('user', 'product',)

    autocomplete_lookup_fields = {
        'fk': ['user', 'product'],
    }

    # noinspection PyMethodMayBeStatic
    def product_kind(self, reservation):
        return reservation.product.kind

    # noinspection PyMethodMayBeStatic
    def product_name(self, reservation):
        return reservation.product.name

    # noinspection PyMethodMayBeStatic
    def product_brand(self, reservation):
        return reservation.product.brand

    # noinspection PyMethodMayBeStatic
    def customer_name(self, reservation):
        return reservation.user.username

    # noinspection PyMethodMayBeStatic
    def customer_email(self, reservation):
        return reservation.user.email

    # noinspection PyMethodMayBeStatic
    def customer_address(self, reservation):
        return reservation.user.address


admin.site.register(Reservations, ReservationsAdmin)
