from django.urls import path
from .views import contatti

app_name='forms_app'

urlpatterns = [
    path('contattaci/', contatti, name='contatti'),
]