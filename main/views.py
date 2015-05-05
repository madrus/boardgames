from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("Hello, World!") # direct message string
    #return render(request, "main/home.html") # render from template
    return render(request, "main/home.html", {'message': 'Hi, here!'}) # render from template with dictionary
