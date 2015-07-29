from django.contrib import admin

from inventoryapp.reservations.admin import ReservationsInline

from inventoryapp.sales.admin import SalesInline
from inventoryapp.user.models import User


class UserAdmin(admin.ModelAdmin):
    inlines = [ReservationsInline, SalesInline]


admin.site.register(User, UserAdmin)
