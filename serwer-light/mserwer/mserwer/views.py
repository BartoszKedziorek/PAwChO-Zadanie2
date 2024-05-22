from django.views import View
from datetime import date
import datetime
from django.shortcuts import render
import pytz
from django.utils.timezone import localtime


class IndexView(View):
    def get(self, request, format=None):

        # polecenie pobierające adres ip klienta
        client_ip = request.META['REMOTE_ADDR']

        # przekazanie adresu ip do szablonu
        return render(request, 'mserwer/index.html', context={
            'ip': client_ip,
        })




