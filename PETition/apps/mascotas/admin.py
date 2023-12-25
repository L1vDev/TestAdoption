from django.contrib import admin
from apps.mascotas.models import Vacunas, Mascotas, Adoption_Register

# Register your models here.
admin.site.register(Vacunas)
admin.site.register(Mascotas)
admin.site.register(Adoption_Register)