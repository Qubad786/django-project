from django.core.urlresolvers import reverse

from django.shortcuts import render, redirect
from django.views.generic import View

from inventoryapp.user.models import User
from inventoryapp.user.forms.sign_up_form import SignUpForm


class SignUpView(View):
    template_name = 'user/sign_up.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, dict(msg='', sign_up_form=form))

    def post(self, request):
        response = None
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('name')
            user_email = form.cleaned_data.get('email')
            user_password = form.cleaned_data.get('password')
            user_address = form.cleaned_data.get('address')
            user_gender = form.cleaned_data.get('gender')
            is_admin = form.cleaned_data.get('is_admin')

            try:
                if is_admin:
                    User.objects.create_superuser(email=user_email, username=user_name, gender=user_gender,
                                                  address=user_address
                                                  , password=user_password)
                    response = redirect(reverse('admin:index'))
                else:
                    User.objects.create_user(email=user_email, username=user_name, gender=user_gender,
                                             address=user_address
                                             , password=user_password)
                    response = redirect('/')
            except ValueError as ex:
                response = render(request, self.template_name, dict(msg=ex.message, sign_up_form=form))

        else:
            response = render(request, self.template_name, dict(msg='Invalid inputs.', sign_up_form=form))

        return response
