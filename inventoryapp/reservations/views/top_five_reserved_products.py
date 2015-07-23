from django.shortcuts import render
from django.views.generic import View
from inventoryapp.reservations.models import Reservations


class TopFiveReservedProductsView(View):
    template_name = 'reservations/top_five_reserved_products.html'

    def get(self, request):
        top_five_reserved_products = Reservations.objects.get_top_five_reserved_products()
        return render(request, self.template_name, dict(top_five_reserved_products=top_five_reserved_products))

