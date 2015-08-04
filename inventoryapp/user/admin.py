from django.contrib import admin

from inventoryapp.reservations.admin import ReservationsInline
from inventoryapp.sales.admin import SalesInline
from inventoryapp.user.models import User


class UserAdmin(admin.ModelAdmin):
    inlines = [ReservationsInline, SalesInline]
    list_display = ('email', 'username', 'gender', 'address', 'is_active', 'is_admin')
    list_filter = ('email', 'username', 'gender', 'is_active', 'is_admin')
    search_fields = ('username', 'email', 'address')

    fieldsets = (
        (
            'Edit User Information', {
                'classes': ('grp-collapse grp-open',),
                'fields': ('email', 'username', 'password', 'gender', 'address', 'is_active', 'is_admin', 'last_login'),
            }
        ),
    )


admin.site.register(User, UserAdmin)
