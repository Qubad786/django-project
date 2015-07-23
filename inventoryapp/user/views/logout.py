from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth import logout


class LogoutView(View):
    template_name = None

    # noinspection PyMethodMayBeStatic
    def get(self, request):
        logout(request)
        return redirect('/')

