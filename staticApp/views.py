from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView
from staticApp.models import Images
from staticApp.forms import Image_Form

# Create your views here.
class Image_View(TemplateView):
    template_name = "images.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Images.objects.all()
        return context
    
class Add_Image_View(CreateView):
    model = Images
    form_class = Image_Form
    template_name = 'addimagen.html'
    success_url = reverse_lazy('image')