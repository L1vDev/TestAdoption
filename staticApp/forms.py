from django.forms import ModelForm
from staticApp.models import Images

class Image_Form(ModelForm):

    class Meta:
        model = Images
        fields='__all__'