from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from inventoryapp.reservations.views.order import OrderView
from inventoryapp.reservations.views.orders import OrdersView
from inventoryapp.reservations.views.top_five_customers import TopFiveCustomersView
from inventoryapp.reservations.views.top_five_reserved_products import TopFiveReservedProductsView


urlpatterns = [
    url(r'^order/$', login_required(OrderView.as_view()), name='order'),
    url(r'^all/$', login_required(OrdersView.as_view()), name='orders'),
    url(r'^top-5-ordered-products/$', login_required(TopFiveReservedProductsView.as_view()),
        name='top_five_reserved_products'),
    url(r'^top-5-customers/$', login_required(TopFiveCustomersView.as_view()), name='top_five_customers')
]