from django.urls import path
from apps.mascotas.views import *

urlpatterns=[
    path('', Index_View.as_view(), name='index'),
    path('registrar/mascota', Registrar_Mascota_View.as_view(), name='registrarmascota'),
    path('mascotas', Mascotas_Presentes_View.as_view(), name='mascotas'),
    path('infomascota/<int:pk>', Info_Mascota_View.as_view(), name='infomascota'),
    path('adoption', Adoption_View.as_view() , name='adoption'),
    path('editar/mascota/<int:pk>', Editar_Mascota_View.as_view(),name='editarmascota'),
    path('eliminar/mascota/<int:pk>', Eliminar_Mascota_View.as_view(),name='eliminarmascota'),
    path('registrar/vacuna', Registrar_Vacuna_View.as_view(), name='registrarvacuna'),
    path('vacunas', Vacunas_View.as_view(),name='vacunas'),
    path('eliminar/vacuna/<int:pk>', Delete_Vacuna_View.as_view(),name='eliminarvacuna'),
]