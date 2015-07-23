from django.shortcuts import render
from django.views.generic import View

from djangotestapp.products.models import Products


class ProductsView(View):
    template_name = 'products/all_products.html'

    def get(self, request):
        return render(request, self.template_name, dict(products=Products.objects.all()))

