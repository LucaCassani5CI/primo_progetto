from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Articolo, Giornalista
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import JsonResponse

# Create your views here.
"""
def home (request):
    #return HttpResponse("<h1>HomePage news!</h1>")
    a = ""
    g = ""
    for art in Articolo.objects.all():
        a += (art.titolo + "<br>")
    
    for gio in Giornalista.objects.all():
        g += (gio.nome + "<br>")
    response = "Articoli:<br>"+ a + "<br>Giornalisti:<br>" + g 

    return HttpResponse ("<h1>"+ response+ "</h1>")
"""

"""
def home (request):
    #adesso a e g sono 2 array e non più delle stringhe
    a = []
    g = []
    for art in Articolo.objects.all():
        a.append(art.titolo)
    
    for gio in Giornalista.objects.all():
        g.append(gio.nome)
    response = str(a) + "<br>" + str(g)
    print(response)

    return HttpResponse ("<h1>"+ response+ "</h1>")
"""
def home (request):
    #ora prendiamo tutti gli articoli e tutti i giornalisti e li mettiamo in un dizionario
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render (request, "homepage_news.html", context) #passiamo il dizionario alla pagina 

def articoloDetailView(request, pk):
    #articolo = Articolo.object.get(pk=pk)
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo": articolo}
    return render(request, "articolo_detail.html", context)

class ArticoloDetailViewCB(DetailView):
    model = Articolo
    template_name = "articolo_detail.html"

class ArticoloListView(ListView):
    model = Articolo
    template_name = "lista_articoli.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articoli"] = Articolo.objects.all() 
        return context

class GiornalistaDetailViewCB(DetailView):
    model = Giornalista
    template_name = "giornalista_detail.html"

class GiornalistaListView(ListView):
    model = Giornalista
    template_name = "lista_giornalisti.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["giornalisti"] = Giornalista.objects.all() 
        return context

def giornalisti_list_api(request):
    giornalisti=Giornalista.objects.all()
    data={'giornalisti':list(giornalisti.values("pk","nome","cognome"))}
    response=JsonResponse(data)
    return response

def giornalisti_api(request, pk):
    try:
        giornalista=Giornalista.objects.get(pk=pk)
        data={'giornalista':{
            "nome":giornalista.nome,
            "cognome":giornalista.cognome,
        }
        }
        response=JsonResponse(data)
    except Giornalista.DoesNotExist:
        response=JsonResponse({
            "error":{
                "code":404,
                "message":"Giornalista non trovato"
            }
        },
        status=404)
    return response


def articoli_list_api(request):
    articoli=Articolo.objects.all()
    data={'articoli':list(articoli.values("pk","titolo","contenuto","giornalista"))}
    response=JsonResponse(data)
    return response

def articoli_api(request, pk):
    try:
        articolo=Articolo.objects.get(pk=pk)
        data={'articolo':{
            "titolo":articolo.titolo,
            "contenuto":articolo.contenuto,
            "giornalista":articolo.giornalista.nome + " " + articolo.giornalista.cognome,
        }
        }
        response=JsonResponse(data)
    except Articolo.DoesNotExist:
        response=JsonResponse({
            "error":{
                "code":404,
                "message":"Articolo non trovato"
            }
        },
        status=404)
    return response