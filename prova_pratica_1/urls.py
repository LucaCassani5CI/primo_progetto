from django.urls import path
from .views import view_a, view_b, view_c

app_name="prova_pratica_1"
urlpatterns=[
    path('materie',view_a, name='materie'),
    path('voti', view_b, name='voti'),
    path('media', view_c, name='media'),
]