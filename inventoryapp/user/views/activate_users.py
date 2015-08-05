from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import View
from inventoryapp.user.models import User


class ActivateUsersView(View):

    # noinspection PyMethodMayBeStatic
    def get(self, request):

        users = User.objects.all();
        for user in users:
            if not user.is_staff:
                if not user.is_active:
                    user.is_active = True
                    user.save()

        return redirect(reverse('admin:index'))