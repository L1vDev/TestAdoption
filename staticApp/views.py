from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from staticApp.models import Images

# Create your views here.
class Image_View(TemplateView):
    template_name = "images.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Images.objects.all()
        return context