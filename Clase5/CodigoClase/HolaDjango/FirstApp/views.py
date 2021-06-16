from django.shortcuts import render, HttpResponse

# Create your views here.

def newApp(request):
    return HttpResponse("Esta es una nueva app")