from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Esta es mi primera app")


def showTemplate(request):
    context = {
        "id_grupo": 1,
        "titulo_proyecto": "Este es nuestro tema",
        "integrantes": ["Patricio", "Alonso", "María"]
    }
    return render(request, "showtemplate.html", context=context)