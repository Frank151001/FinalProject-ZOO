from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name="pages/home.html"

class AboutPageView(TemplateView):
    template_name="pages/about.html"

class AnimalsPageView(TemplateView):
    template_name="pages/animals.html"

class TicketsPageView(TemplateView):
    template_name="pages/tickets.html"
# Create your views here.
