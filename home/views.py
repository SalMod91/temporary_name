from django.shortcuts import render
from django.views.generic import TemplateView

class HomePage(TemplateView):
    """
    View for home page
    """
    template_name = "index.html"
