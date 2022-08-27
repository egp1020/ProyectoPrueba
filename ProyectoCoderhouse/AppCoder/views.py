from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def familiar(request):
    return HttpResponse("Hola people!")