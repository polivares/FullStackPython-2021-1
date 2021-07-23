from django.shortcuts import render, redirect
from TestApp.models import *
import bcrypt

# Create your views here.

def index(request):
    return render(request, 'index.html')

def signin(request):
    if request.method == 'POST':
        # Hacer la verificación de login antes de mostrar la página
        email = request.POST['email']
        passw = request.POST['password']
        usuario = Usuario.objects.get(email=email)
        if bcrypt.checkpw(passw.encode(), usuario.password.encode()):
            # Enviar al usuario a su página dependiendo del tipo de usuario
            # Si es admin, enviarlo a su dashboard
            if usuario.user_level == 9:
                return redirect('/dashboard/admin/')
            elif usuario.user_level == 0:
                return redirect('/dashboard/')

    return render(request, 'signin.html')

def register(request):
    if request.method == 'POST':
        # Verificar que la contraseña enviada sea la misma que la
        # confirmada
        if request.POST['password'] == request.POST['conf_password']:
            email = request.POST['email']
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            passw = request.POST['password']
            user_hash = bcrypt.hashpw(passw.encode(), bcrypt.gensalt()).decode()
            user_level = 0 # Cero representa un usuario normal, 9 el administrador
            # Si no hay ningún registro en la tabla, cambiamos el nivel de usuario a administrador
            if len(Usuario.objects.all()) == 0:
                user_level = 9
            Usuario.objects.create(email=email,
                                   nombre = nombre,
                                   apellido = apellido,
                                   password = user_hash,
                                   user_level = user_level)
            
    return render(request, 'register.html')

def dashboard_admin(request):
    return render(request, 'dashboard_admin.html')

def users_new(request):
    return render(request, 'users_new.html')

def show_user(request):
    return render(request, 'show_user.html')

def edit_user(request):
    return render(request, 'edit_user.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def users_edit(request):
    return render(request, 'users_edit.html')
