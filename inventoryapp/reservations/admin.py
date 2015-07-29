from django.contrib import admin

from inventoryapp.reservations.models import Reservations


class ReservationsInline(admin.TabularInline):
    model = Reservations
    extra = 1


class ReservationsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Reservations, ReservationsAdmin)
