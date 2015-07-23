from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from djangotestapp.sales.views.sales import SalesView


urlpatterns = [
    url(r'^sales/$', login_required(SalesView.as_view()), name='sales'),
    ]