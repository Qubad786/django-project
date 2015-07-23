from django.core.urlresolvers import reverse
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import View

from djangotestapp.products.models import Products
from djangotestapp.reservations.forms.order_form import OrderForm
from djangotestapp.reservations.models import Reservations


class OrderView(View):
    template_name = 'reservations/order.html'

    def get(self, request):
        product_id = request.GET.get('product_id')
        request.session['product_id'] = product_id
        product = Products.objects.filter(pk=int(product_id))[0]
        order_form = OrderForm(
            initial={'product_name': product.product_name, 'type': product.type, 'brand': product.brand,
                     'units': self.get_total_units(product.product_name, product.type, product.brand),
                     'price': product.get_unit_selling_price})
        return render(request, self.template_name, dict(order_form=order_form))

    def post(self, request):
        order_form = OrderForm(request.POST)
        response = None
        if order_form.is_valid():
            product_id = request.session.get('product_id')
            units = int(order_form.cleaned_data.get('units'))
            product = Products.objects.filter(pk=int(product_id))[0]
            if self.get_total_units(product.product_name, product.type, product.brand) < units:
                response = render(request, self.template_name,
                                  dict(msg='That many units are not available.', order_form=order_form))
            else:
                Reservations(user=request.user, product=product, ordered_units=units).save()
                response = redirect(reverse('products'))
        else:
            response = render(request, self.template_name,
                              dict(msg='input the units correctly!', order_form=order_form))
        return response

    # noinspection PyMethodMayBeStatic
    def get_total_units(self, product_name, type, brand):
        filter_criteria = Q(product_name=product_name, type=type, brand=brand)
        all_units = Products.objects.filter(filter_criteria).values('units')
        number_of_units = 0
        for units in all_units:
            number_of_units += units.get('units')
        return number_of_units
