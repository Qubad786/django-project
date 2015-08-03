from django.contrib import admin

from inventoryapp.reservations.models import Reservations


class ReservationsInline(admin.TabularInline):
    model = Reservations
    extra = 1


class ReservationsAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_name', 'product_kind', 'ordered_units', 'ordered_on', 'price',)
    list_filter = ('user__email', 'product__name', 'ordered_units', 'ordered_on', 'price')
    search_fields = ('user__email', "user__username", 'product__name', "product__kind")

    # noinspection PyMethodMayBeStatic
    def product_kind(self, reservation):
        return reservation.product.kind

    # noinspection PyMethodMayBeStatic
    def product_name(self, reservation):
        return reservation.product.name


admin.site.register(Reservations, ReservationsAdmin)
