from django.shortcuts import render
from django.views import View
from .models import Partner

class PartnersView(View):

    template = '../templates/partners/sponsors.html'

    def get(self, request, *args, **kwargs):
        PartnerList = Partner.objects.all()
        return render(request, self.template, {'Partners': PartnerList})
