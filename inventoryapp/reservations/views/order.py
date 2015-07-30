from django.core.urlresolvers import reverse
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import View

from inventoryapp.products.models import Products
from inventoryapp.reservations.forms.order_form import OrderForm
from inventoryapp.reservations.models import Reservations


class OrderView(View):
    template_name = 'reservations/order.html'

    def get(self, request):

        product_id = request.GET.get('product_id')
        request.session['product_id'] = product_id
        product = Products.objects.get(pk=int(product_id))

        order_form = OrderForm(
            initial={'name': product.name, 'kind': product.kind, 'brand': product.brand,
                     'units': self.get_total_units(product.name, product.kind, product.brand),
                     'price': product.get_unit_selling_price})

        return render(request, self.template_name, dict(order_form=order_form))

    def post(self, request):

        order_form = OrderForm(request.POST)
        response = None

        if order_form.is_valid():

            product_id = request.session.get('product_id')

            if product_id:

                units = int(order_form.cleaned_data.get('units'))
                product = Products.objects.get(pk=int(product_id))
                if self.get_total_units(product.name, product.kind, product.brand) < units:
                    response = render(request, self.template_name,
                                      dict(msg='That many units are not available.', order_form=order_form))
                else:
                    Reservations(user=request.user, product=product, ordered_units=units).save()
                    response = redirect(reverse('reservations'))
            else:
                response = redirect(reverse('account'))
        else:
            response = render(request, self.template_name,
                              dict(msg='give units correctly!', order_form=order_form))
        return response

    # noinspection PyMethodMayBeStatic
    def get_total_units(self, product_name, kind, brand):
        filter_criteria = Q(name=product_name, kind=kind, brand=brand)
        all_units = Products.objects.filter(filter_criteria).values('units')
        number_of_units = 0
        for units in all_units:
            number_of_units += units.get('units')
        return number_of_units
