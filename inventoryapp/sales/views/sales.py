from django.shortcuts import render
from django.views.generic import View
from inventoryapp.sales.models import Sales


class SalesView(View):
    template_name = 'sales/sales.html'

    def get(self, request):
        return render(request, self.template_name, dict(all_sales=Sales.objects.all()))