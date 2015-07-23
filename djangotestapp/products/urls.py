from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from djangoproject.decoratorts import is_logged_in
from djangotestapp.products.views.add_product import AddProductView
from djangotestapp.products.views.products import ProductsView


urlpatterns = [
    url(r'^add-product/$', login_required(AddProductView.as_view()), name='add_product'),
    url(r'^all/$', login_required(ProductsView.as_view()), name='products'),
    ]