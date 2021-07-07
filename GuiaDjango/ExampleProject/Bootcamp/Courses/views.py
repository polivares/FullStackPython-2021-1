from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    # Acá escribiremos el código de la vista index
    return render(request,'index.html')


def professor(request):
    return render(request, 'professor.html')

def create_course(request):
    return render(request, 'create_course.html')

def student(request):
    return render(request, 'student.html')

