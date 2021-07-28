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
            # Almacenado como variables de sesión
            request.session['email'] = email
            request.session['user_level'] = usuario.user_level
            request.session['name'] = f'{usuario.nombre} {usuario.apellido}'
            # Enviar al usuario a su página dependiendo del tipo de usuario
            # Si es admin, enviarlo a su dashboard. user_level=9 => admin, user_level=0 => normal
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
    # La verificación de sesión debería estar incluida en casi todas las vistas
    if request.session.get('email') == None:
        return redirect('/signin/')
    
    # Si el usuario es normal, no debería entrar a esta vista
    if request.session.get('user_level') == 0:
        return redirect('/dashboard/')
    
    # Si nos llega un POST a la misma página, quiere decir que alguien está intentando 
    # borrar un usuario
    if request.method == 'POST':
        usuario = Usuario.objects.get(id=request.POST['id'])
        usuario.delete()
    # Consultar datos de usuarios en la base de datos
    usuarios = Usuario.objects.all()
    
    context = {
        'usuarios': usuarios,
    }

    return render(request, 'dashboard_admin.html', context=context)

def users_new(request):
    return render(request, 'users_new.html')

def show_user(request):
    return render(request, 'show_user.html')

def edit_user(request):
    return render(request, 'edit_user.html')

def dashboard(request):
    # La verificación de sesión debería estar incluida en casi todas las vistas
    if request.session.get('email') == None:
        return redirect('/signin/')
    
    # Si el usuario es admin, no debería entrar a esta vista
    if request.session.get('user_level') == 9:
        return redirect('/dashboard/admin/')
    
    # Consultar datos de usuarios en la base de datos
    usuarios = Usuario.objects.all()
    
    context = {
        'usuarios': usuarios,
    }

    return render(request, 'dashboard.html', context=context)

def users_edit(request):
    return render(request, 'users_edit.html')
