from django.db import models

# Create your models here.

class Images(models.Model):
    img = models.ImageField(verbose_name="Imagen", upload_to="images")