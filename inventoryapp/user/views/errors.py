from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View


def view_404(request):
    response = render(request, template_name='user/404.html', context_instance=RequestContext(request))
    response.status_code = 404
    return response