from django.urls import  path
from . import views

urlpatterns = [

    path('',views.vistaFormulario, name = "vistaFormulario")
]