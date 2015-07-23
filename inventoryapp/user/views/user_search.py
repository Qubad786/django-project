from django.views.generic import View
from django.shortcuts import render
from django.db.models import Q

from inventoryapp.user.forms.user_search_form import UserSearchForm
from inventoryapp.user.models import User


class UserSearchView(View):
    template_name = 'user/user_search.html'

    def get(self, request):
        return render(request=request, template_name=self.template_name,
                      dictionary=dict(user_search_form=UserSearchForm()))

    def post(self, request):
        user_search_form = UserSearchForm(request.POST)
        if user_search_form.is_valid():
            email = user_search_form.cleaned_data.get('email')
            start_date = user_search_form.cleaned_data.get('start_date')
            end_date = user_search_form.cleaned_data.get('end_date')
            result_basis = user_search_form.cleaned_data.get('result_should_include')

            return render(request=request, template_name=self.template_name,
                          dictionary=dict(users=self.get_matching_users(email, start_date, end_date, result_basis),
                                          user_search_form=user_search_form, result_basis=result_basis))

    # noinspection PyMethodMayBeStatic
    def get_matching_users(self, email, start_date, end_date, result_basis):

        filter_criteria = Q()
        if email:
            filter_criteria = filter_criteria & Q(email=email)
            if start_date and end_date:
                filter_criteria = filter_criteria & Q(date_joined__range=[start_date, end_date])

        elif start_date and end_date:
            filter_criteria = filter_criteria & Q(date_joined__range=[start_date, end_date])

        matched_users = User.objects.filter(filter_criteria)
        return matched_users.values(result_basis) if result_basis else matched_users



