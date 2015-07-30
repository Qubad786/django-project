from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View

from inventoryapp.user.forms.profile_form import ProfileForm


class EditProfileView(View):
    template_name = 'user/edit_profile.html'

    def get(self, request):
        user_profile = request.user
        form = ProfileForm(initial={'email': user_profile.email, 'name': user_profile.username,
                                    'address': user_profile.address, 'gender': user_profile.gender})

        return render(request, self.template_name, dict(msg='', profile_form=form))

    def post(self, request):
        response = None
        form = ProfileForm(request.POST)
        if form.is_valid():

            user = request.user
            user.username = form.cleaned_data.get('name')
            user.set_password(form.cleaned_data.get('password'))
            user.gender = form.cleaned_data.get('gender')
            user.address = form.cleaned_data.get('address')
            user.save()

            response = redirect('/')
        else:
            response = render(request, self.template_name, dict(msg='Invalid inputs.', profile_form=form))

        return response