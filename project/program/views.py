from django.shortcuts import render
from django.views import View
from .models import Presenter

class SpeakersView(View):

    template = '../templates/speakers.html'

    def get(self, request, *args, **kwargs):
        PresenterList = Presenter.speakers.all()
        return render(request, self.template, {'Presenters': PresenterList})
