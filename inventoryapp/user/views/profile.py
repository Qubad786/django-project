from django.shortcuts import render
from django.views.generic import View


class ProfileView(View):
    template_name = 'user/profile.html'

    def get(self, request):
        return render(request, self.template_name, dict(user_profile=request.user))