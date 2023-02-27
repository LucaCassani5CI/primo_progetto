from django.urls import path
from .views import home, ArticoloDetailViewCB, ArticoloListView, GiornalistaDetailViewCB, GiornalistaListView, giornalisti_list_api, giornalisti_api, articoli_list_api, articoli_api, tabella_giornalisti, tabella_articoli #articoloDetailView

app_name = 'news'

urlpatterns = [
    path('', home, name="homeview"),
    #path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("articoli/<int:pk>", ArticoloDetailViewCB.as_view(), name="articolo_detail"),
    path("lista_articoli/", ArticoloListView.as_view(), name="lista_articoli"),
    path("giornalisti/<int:pk>", GiornalistaDetailViewCB.as_view(), name="giornalista_detail"),
    path("lista_giornalisti/", GiornalistaListView.as_view(), name="lista_giornalisti"),
    path("lista_giornalisti_api/",giornalisti_list_api, name="giornalisti_list_api"),
    path("giornalisto_api/<int:pk>", giornalisti_api, name="giornalisti_api"),
    path("lista_articoli_api/",articoli_list_api, name="articoli_list_api"),
    path("articolo_api/<int:pk>", articoli_api, name="articoli_api"),
    path("tabella_giornalisti/", tabella_giornalisti, name="tabella_giornalisti"),
    path("tabella_articoli/", tabella_articoli, name="tabella_articoli"),

]