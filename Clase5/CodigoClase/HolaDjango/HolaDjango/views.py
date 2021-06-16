from django.shortcuts import HttpResponse


def hello(response):
    return HttpResponse("hola mundo!")