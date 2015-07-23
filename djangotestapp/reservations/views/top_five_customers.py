from django.shortcuts import render
from django.views.generic import View
from djangotestapp.reservations.models import Reservations


class TopFiveCustomersView(View):
    template_name = 'reservations/top_five_customers.html'

    def get(self, request):
        top_five_customers = Reservations.objects.get_top_five_customers_based_on_reservations()
        return render(request, self.template_name, dict(top_five_customers=top_five_customers))