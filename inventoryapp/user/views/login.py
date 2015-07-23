from datetime import datetime

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from dateutil import rrule
from dateutil.parser import parse
from inventoryapp.user.forms.sign_in_form import SignInForm


SCRIPT = '<script type="text/javascript"> ' \
         'alert("You have logged in second time"); ' \
         'window.parent.location.href = "account"; ' \
         '</script>'


class LoginView(View):
    template_name = 'user/login.html'

    def get(self, request):

        username = request.COOKIES.get('username')
        form = SignInForm(initial={'name': username, 'remember_me': True}) if username else SignInForm()
        return render(request, self.template_name, dict(msg='', sign_in_form=form))

    def post(self, request):

        response = None
        form = SignInForm(request.POST)
        response_message = ''

        if form.is_valid():

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data.get('remember_me')
            user = authenticate(email=email, password=password)

            if user is not None:
                if user.is_active:

                    login(request, user)
                    response = redirect(reverse('account'))
                    response.set_cookie('email', email) if remember_me else response.delete_cookie('email')

                else:
                    response_message = 'Account has been disabled'
            else:
                response_message = 'Username or password is incorrect.'
        else:
            response_message = 'Please fill in the fields'

        if response_message:
            response = render(request, self.template_name, dict(msg=response_message, sign_in_form=form))

        return response

    # these helpers are not used anywhere yet
    def save_or_get_login_count(self, request):
        login_count = None
        if not request.session.exists(request.session.session_key):
            request.session.create()
            login_count = self.initialize_login_datetime(request=request)
        else:
            login_datetime_dict = request.session.get('login_datetime', True)

            begin_date = parse(login_datetime_dict.get('initial_login_datetime'))
            current_date = parse(login_datetime_dict.get('current_login_datetime'))

            if self.two_months_are_complete(date_begin=begin_date,date_end=current_date):
                login_count = self.initialize_login_datetime(request=request)
            else:
                login_count = self.update_login_datetime(request=request)

        return login_count

    # noinspection PyMethodMayBeStatic
    def two_months_are_complete(self, date_begin, date_end):
        number_of_months = len(list(rrule.rrule(rrule.MONTHLY, dtstart=date_begin, until=date_end))) - 1
        is_complete = False
        if number_of_months >= 2:
            is_complete = True
        return is_complete

    # noinspection PyMethodMayBeStatic
    def initialize_login_datetime(self, request):
        datetime_now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        request.session['login_datetime'] = dict(initial_login_datetime=datetime_now
                                                 , current_login_datetime=datetime_now, login_count=1)
        return 1

    # noinspection PyMethodMayBeStatic
    def update_login_datetime(self, request):
        login_datetime_dict = request.session['login_datetime']
        login_datetime_dict['current_login_datetime'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        login_datetime_dict['login_count'] += 1
        return login_datetime_dict['login_count']



