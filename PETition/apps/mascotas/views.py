from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, UpdateView, DeleteView
from apps.mascotas.models import Mascotas, Adoption_Register, Vacunas
from apps.mascotas.forms import Registrar_Mascota, Adoption_Mascota, Registrar_Vacuna, Editar_Mascota

class Index_View(TemplateView):
    template_name = 'mascotas/index.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['page_name'] = "Inicio"
        context['mascotas'] = Mascotas.objects.order_by('-entry_date')[:4]
        return context
    
class Donation_View(TemplateView):
    template_name = 'mascotas/donation.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['page_name'] = "Donacion"
        context['url'] = 'Donar'
        return context
    
class Help_View(TemplateView):
    template_name = 'mascotas/help.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['page_name'] = "Preguntas Frecuentes"
        context['url'] = 'Ayuda'
        return context

class Mascotas_Presentes_View(ListView):
    model = Mascotas
    template_name = 'mascotas/mascotas.html'

    def get_context_data(self, **kwargs):
        context=super(Mascotas_Presentes_View, self).get_context_data(**kwargs)
        context['mascotas_list'] = Mascotas.objects.filter(is_adopted = False)
        context['page_name'] = "Mascotas Presentes"
        context['url'] = 'Mascotas'
        return context
    
    def post(self, request, *args, **kwargs):
        register_form = Registrar_Mascota(request.POST)
        adoption_form = Adoption_Mascota(request.POST)
        if adoption_form.is_valid():
            adoption_form.save()
        if register_form.is_valid():
            register_form.save()
        return self.get(request, *args, **kwargs)
    
class Info_Mascota_View(ListView):
    model=Mascotas
    template_name = 'mascotas/infomascota.html'
    

    def get_context_data(self, **kwargs):
        mascota = Mascotas.objects.get(id=self.kwargs['pk'])
        context =  super().get_context_data(**kwargs)
        context['page_name'] = "Ver Mas"
        context['url'] = f"Info / {Mascotas.objects.get(id=self.kwargs['pk'])}"
        context['mascota'] = mascota
        context['vacunas'] = mascota.vacunas.all()
        return context
  
class Registrar_Mascota_View(CreateView):
    model = Mascotas
    form_class = Registrar_Mascota
    template_name = 'mascotas/registrarmascota.html'
    success_url = reverse_lazy('mascotas')

    
    def get_context_data(self, **kwargs):
        context=super(Registrar_Mascota_View, self).get_context_data(**kwargs)
        context['page_name'] = "Registrar Mascota"
        context['url'] = 'Registrar / Mascota'
        return context

class Editar_Mascota_View(UpdateView):
    model = Mascotas
    form_class = Editar_Mascota 
    template_name = 'mascotas/editarmascota.html'
    success_url = reverse_lazy('mascotas')

    def get_context_data(self, **kwargs):
        context=super(Editar_Mascota_View, self).get_context_data(**kwargs)
        context['page_name'] = "Editar Mascota"
        context['url'] = 'Editar / Mascota'
        return context

class Eliminar_Mascota_View(DeleteView):
    model = Mascotas
    template_name = "mascotas/delete.html"
    success_url = reverse_lazy("mascotas")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Eliminar Mascota"
        context['eliminar'] = self.get_object()
        context['url'] = f"Eliminar / {self.get_object()}"
        return context

class Adoption_View(CreateView):
    model = Adoption_Register
    form_class = Adoption_Mascota
    template_name = 'mascotas/adoption.html'
    success_url = reverse_lazy('mascotas')

    def get_context_data(self, **kwargs):
        context=super(Adoption_View, self).get_context_data(**kwargs)
        context['page_name'] = "Adoptar Mascota"
        context['url'] = f"Adoptar / {self.get_initial()['mascota']}"
        return context

    def get_initial(self):
        initial = super().get_initial()
        id_mascota = self.request.GET.get('mascota_id')
        if id_mascota:
            mascota = Mascotas.objects.get(id=id_mascota)
            initial['mascota'] = mascota
        return initial

    
class Vacunas_View(ListView):
    model = Vacunas
    template_name = "mascotas/vacunas.html"

    def get_context_data(self, **kwargs):
        context=super(Vacunas_View, self).get_context_data(**kwargs)
        context['page_name'] = "Vacunas"
        context['vacunas_list'] = Vacunas.objects.all()
        context['url'] = "Vacunas"
        return context
    
    def post(self, request, *args, **kwargs):
        form = Registrar_Vacuna(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request, *args, **kwargs)
  

class Registrar_Vacuna_View(CreateView):
    model = Vacunas
    form_class = Registrar_Vacuna
    template_name = 'mascotas/registrarvacuna.html'
    success_url = reverse_lazy('vacunas')

    def get_context_data(self, **kwargs):
        context=super(Registrar_Vacuna_View, self).get_context_data(**kwargs)
        context['page_name'] = "Registrar Vacuna"
        context['url'] = "Registrar / Vacuna"
        return context
    
    
class Delete_Vacuna_View(DeleteView):
    model = Vacunas
    template_name = "mascotas/delete.html"
    success_url = reverse_lazy("vacunas")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Eliminar Vacuna"
        context['eliminar'] = self.get_object()
        context['url'] = f"Eliminar / {self.get_object()}"
        return context