from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic import View

from inventoryapp.products.forms.add_product_form import AddProductForm
from inventoryapp.products.models import Products


class AddProductView(View):
    template_name = 'products/add_product.html'

    def get(self, request):
        return render(request, self.template_name, dict(add_product_form=AddProductForm()))

    def post(self, request):
        add_product_form = AddProductForm(request.POST)
        response = None

        if add_product_form.is_valid():
            product_name = add_product_form.cleaned_data.get('product_name')
            type = add_product_form.cleaned_data.get('type')
            brand = add_product_form.cleaned_data.get('brand')
            units = add_product_form.cleaned_data.get('units')
            stock_price = add_product_form.cleaned_data.get('stock_price')
            profit_factor = add_product_form.cleaned_data.get('profit_in_percentage')
            Products(product_name=product_name, type=type, brand=brand, units=units,
                     actual_unit_price=stock_price, profit_factor=profit_factor).save()
            response = redirect(reverse('account'))
        else:
            response = render(request, self.template_name, dict(add_product_form=add_product_form))

        return response

