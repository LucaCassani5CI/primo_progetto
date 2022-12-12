from django.shortcuts import render

# Create your views here.

def view_a (request):
    materie = ["Matematica","Italiano","Inglese","Storia","Geografia"]
    context={
       'materie': materie,
    }
    return render(request,"materie.html", context)

def view_b (request):

    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    
    

    context={
        'voti':voti,
    }
    return render(request,"voti.html", context)

def view_c(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    chiavi=[]
    for studente in voti.keys():
        chiavi.append(studente) 
    
    dic_voti={}
    for chiave in chiavi:
        somma=0
        media=0
        for i in range(0,len(voti[chiave])):
            somma+=voti[chiave][i][1]
        media=somma/len(voti[chiave])
        dic_voti[chiave]=media
    print( dic_voti )
    

    context={
        'dic_voti':dic_voti
    }
    return render(request,"media.html", context)