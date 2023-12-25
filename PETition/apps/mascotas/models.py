from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MinLengthValidator, MaxLengthValidator
#import os
from datetime import datetime

# Create your models here.
class Vacunas(models.Model):
    name_vacuna = models.CharField(max_length=20, verbose_name='Vacuna: ', unique=True)

    def __str__(self) -> str:
        return self.name_vacuna
    


class Mascotas(models.Model):

    name = models.CharField(max_length=25, verbose_name='Nombre:')
    age = models.IntegerField(verbose_name='Edad:')
    description = models.TextField(max_length=150, verbose_name="Descripcion:", blank=True)
    esteril = models.BooleanField(verbose_name="Esteril: ")
    entry_date = models.DateField(auto_now_add=True)
    exit_date = models.DateField(blank=True, null=True)
    is_adopted = models.BooleanField(default=False)
    vacunas = models.ManyToManyField(Vacunas,blank=True, verbose_name='Vacunas:')
    imagen = models.ImageField(verbose_name="Imagen", default="nopicture.jpg", upload_to="images/")

    
    def __str__(self) -> str:
        return self.name

class Adoption_Register(models.Model):
    identity = models.CharField(max_length=11, validators=[MinLengthValidator(11), MaxLengthValidator(11)],verbose_name='CI')
    first_name_adopter = models.CharField(max_length=25, verbose_name='Nombre')
    last_name_adopter = models.CharField(max_length=75, verbose_name='Apellidos')
    email = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(max_length=11, verbose_name='Telefono')
    adoption_date = models.DateField(auto_now_add=True)
    mascota = models.ForeignKey(Mascotas, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.first_name_adopter


@receiver(post_save, sender=Adoption_Register)
def update_date(sender, instance, **kwargs):
    mascota = instance.mascota
    if mascota.exit_date==None:
        mascota.exit_date = instance.adoption_date
        mascota.is_adopted = True
        mascota.save()