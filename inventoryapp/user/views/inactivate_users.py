from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic import View
from inventoryapp.user.models import User


class InactivateUsersView(View):

    # noinspection PyMethodMayBeStatic
    def get(self, request):

        users = User.objects.all();
        for user in users:
            if not user.is_staff:
                if user.is_active:
                    user.is_active = False
                    user.save()

        return redirect(reverse('admin:index'))
