from django.shortcuts import render
from .models import pepega

# Create your views here.

def index(request):

    pepe1 = pepega.objects.all()

    return render(request, "index.html", {'pepe1':pepe1})
    