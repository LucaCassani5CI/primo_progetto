from django.shortcuts import render
import random

def index1(request):
    return render(request,"index1.html")

def somma(request):
    n1=random.randint(0,10)
    n2=random.randint(0,10)
    somma=n1+n2
    context={
       'n1': n1,
       'n2': n2,
       'somma': somma,
    }
    return render(request,"maxmin.html", context)

def media(request):
    lista=[]
    NUMERI=30
    somma=0
    for i in range (0,NUMERI):
        n=random.randint(1,10)
        lista.append(n)
        somma+=n
    media=somma/NUMERI
    media=round(media, 2)
    context={
        'lista':lista,
        'media':media,
    }
    return render(request,"media.html", context)

