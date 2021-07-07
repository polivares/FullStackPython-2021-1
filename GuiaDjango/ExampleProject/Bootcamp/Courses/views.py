from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    # Acá escribiremos el código de la vista index
    return render(request,'index.html')


def professor(request):
    pass

def create_course(request):
    pass

def student(request):
    return render(request, 'student.html')

