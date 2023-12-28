from django.urls import path
from staticApp.views import *

urlpatterns=[
    path('', Image_View.as_view(),name="image")
]