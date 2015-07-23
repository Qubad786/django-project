from datetime import datetime

from django.shortcuts import render
from django.views.generic import View
from bs4 import BeautifulSoup
import requests

from inventoryapp.user.forms.url_form import UrlForm
from inventoryapp.user.models import *


class AccountView(View):
    template_name = 'user/account.html'

    def get(self, request):
        return render(request, self.template_name, dict(username=request.user.username, url_form=UrlForm()))

    def post(self, request):
        form = UrlForm(request.POST)
        last_updated = None
        response = None

        if form.is_valid():

            url = request.POST['url']
            url_object = UrlData.objects.filter(url=url)

            if url_object.exists():
                url_object = url_object[0]
            else:
                response = requests.get(url)
                soup = BeautifulSoup(response.content)
                size = int(format(int(response.headers['content-length']) / 1024, '.0f'))

                tags_count = len(soup.find_all())
                meta_tags_count = len(soup.find_all('meta'))

                url_object = UrlData(url=url, tags_count=tags_count, meta_tags_count=meta_tags_count,
                                     size=size)

                last_updated = url_object.date_time
                url_object.date_time = datetime.now()
                url_object.save()

                links_objects = []
                for anchor in soup.find_all('a', href=True):
                    if anchor.get('href'):
                        link_object = Anchors(url=url_object, link=anchor['href'])
                        links_objects.append(link_object)

                Anchors.objects.bulk_create(links_objects)

            response = render(
                request,
                'user/result.html',
                dict(url_object=url_object, last_updated=last_updated)
            )

        else:
            response = render(request, self.template_name, dict(username=request.user.username, url_form=form))

        return response