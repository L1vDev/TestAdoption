from typing import Any
from django.forms.utils import ErrorList
from django.forms import ModelForm, ValidationError, ModelChoiceField, FloatField
from apps.mascotas.models import Mascotas, Adoption_Register, Vacunas

class Registrar_Mascota(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for form in self.visible_fields():
            if form.field != self.fields['esteril']:
                form.field.widget.attrs['class'] = 'form-control'
         
        
        self.fields['name'].widget.attrs['placeholder'] = 'Introduzca un nombre'
        self.fields['age'].widget.attrs['placeholder'] = 'Edad en Años'

    class Meta:
        model = Mascotas
        fields = ['name', 'age', 'description', 'vacunas','esteril','imagen']
    
    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get('age')
        img = cleaned_data.get('imagen')
        if img != "nopicture.jpg":
            cleaned_data.get('imagen').name = f"{cleaned_data.get('name')}_{img.name}"
        if age and age<0:
            raise ValidationError({"age":"La edad no puede ser negativa"})
        return cleaned_data
        
class Adoption_Mascota(ModelForm):
    mascota = ModelChoiceField(queryset=Mascotas.objects.filter(is_adopted = False))

    def __init__(self, *args, **kwargs):
        id_mascota = kwargs.pop('mascota_id', None)
        super().__init__(*args, **kwargs)

        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

        
        if id_mascota:
            mascota = Mascotas.objects.get(id=id_mascota)
            self.fields['mascota'].initial = mascota

    class Meta:
        model = Adoption_Register
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        identity = cleaned_data.get('identity')
        phone = cleaned_data.get('phone_number')
        if not identity.isdigit() or len(identity)!=11:
            raise ValidationError({"identity":"El CI debe contener 11 numeros"})
        if not phone.isdigit() or len(phone)<8:
            raise ValidationError({"phone_number":"El telefono debe contener al menos 8 digitos"})
        return cleaned_data

class Registrar_Vacuna(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        

    class Meta:
        model = Vacunas
        fields = '__all__'

    
    def clean(self):
        cleaned_data = super().clean()
        vacuna = cleaned_data.get('name_vacuna').lower()
        if vacuna == Vacunas.objects.get(name_vacuna=vacuna).name_vacuna:
            raise ValidationError({"name_vacuna":"Ya existe esta vacuna"})
        cleaned_data['name_vacuna'] = vacuna
        return cleaned_data

class Editar_Mascota(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for form in self.visible_fields():
            if form.field != self.fields['esteril']:
                form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Mascotas
        fields = ['name', 'age', 'description', 'vacunas','esteril','imagen']

    def clean(self):
        cleaned_data = super().clean()
        if self.get_initial_for_field(self.fields['esteril'],'esteril') and not cleaned_data.get('esteril'):
            print("Error de esterilidad")
            raise ValidationError({"esteril":"Error de Esterilidad"})
        if self.get_initial_for_field(self.fields['imagen'],'imagen') != cleaned_data.get('imagen'):
            img = cleaned_data.get('imagen')
            cleaned_data.get('imagen').name = f"{cleaned_data.get('name')}_{img.name}"
        return cleaned_data
