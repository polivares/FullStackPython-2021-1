from django.shortcuts import HttpResponse

def hola(response):
    return HttpResponse("hola mundo!")


def adios(response):
    return HttpResponse("Mensaje de despedida")

def sendInfo(response, info):
    doc = f"El número enviado es {info}"
    return HttpResponse(doc)