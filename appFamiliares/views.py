from django.shortcuts import render
from .models import Familiares

# Create your views here.
def home(request):
    return render(request, 'appFamiliares/home.html')

def familiares(request):
    familiares = Familiares.objects.all()
    datos = {
        'familiar' : familiares
    }
    return render(request, 'appFamiliares/familiares.html', datos)

