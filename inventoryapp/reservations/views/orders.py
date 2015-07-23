from django.shortcuts import render
from django.views.generic import View
from inventoryapp.reservations.models import Reservations
from inventoryapp.sales.models import Sales


class OrdersView(View):
    template_name = 'reservations/orders.html'

    def get(self, request):
        reservations = request.user.reservations.all()
        return render(request, self.template_name, dict(reservations=reservations))

    def post(self, request):
        reservation_id = request.POST.get('reservation_id')
        if reservation_id:
            order = Reservations.objects.filter(pk=int(reservation_id))[0]
            Sales(user=order.user, product=order.product, units=order.ordered_units).save()
            order.delete()
        reservations = request.user.reservations.all()
        return render(request, self.template_name, dict(reservations=reservations))

