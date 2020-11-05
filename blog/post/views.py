from django.shortcuts import render
from django.urls.conf import path
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "home.html"

    def get_context_data(self, request, *args, **kwargs):
        pass
