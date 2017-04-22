from django.shortcuts import render,redirect
from django.http import Http404
from .models import Reminder
# Create your views here.

def index(request):
    #Queryset
    # SELEC * FROM Reminder
    remainders = Reminder.objects.all()
    print (remainders)
    return render(request,"landing/index.html",{"recordatorios":remainders})
        
        
def agregar(request):
    if request.method == 'POST':
        remainder = Reminder()
        remainder.titulo = request.POST['titulo']
        remainder.descripcion = request.POST['descripcion']
        remainder.prioridad = request.POST['prioridad']
        remainder.save()
        return redirect('landing:index')
    else:
        return render(request,"landing/agregar.html")

def detalle(request,pk):

    try:
        remainder = Reminder.objects.get(id=pk)

    except:
        raise Http404

    return render(request,'landing/detalle.html',{"recordatorio":remainder})