from django.urls import path
from .views import index1, somma, media

app_name="prova_pratica_0"
urlpatterns=[
    path('',index1, name='index1'),
    path('somma',somma, name='somma'),
    path('media', media, name='media'),
]