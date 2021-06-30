from django.shortcuts import render

# Create your views here.

grupos = []

def registro(request):
    if len(grupos) == 0:
        id = 1
    else:
        id = grupos[-1].id + 1
    context = {
        'id': id,
    }
    return render(request,'register.html', context=context)


def listado(request):
    if request.method == "POST":
        if len(grupos) == 0:
            id = 1
        else:
            id = grupos[-1].id + 1

        integrante1 = request.POST['integrante1']
        integrante2 = request.POST['integrante2']
        integrante3 = request.POST['integrante3']
        integrantes = [integrante1, integrante2, integrante3]
        tema = request.POST['project_title']
        descripcion = request.POST['project_description']
        group = Grupo(id, integrantes, tema, descripcion)
        grupos.append(group)
    context = {
        'grupos': grupos,
    }
    return render(request,'list_groups.html', context=context)


class Grupo:
    def __init__(self, id, integrantes, tema, descripcion):
        self.id = id
        self.integrantes = integrantes
        self.tema = tema
        self.descripcion = descripcion