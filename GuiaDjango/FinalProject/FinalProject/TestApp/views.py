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
    if request.method == 'POST':
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
        return redirect('/dashboard/admin')
    return render(request, 'users_new.html')

def show_user(request, user_id):
    usuario_origen = Usuario.objects.get(email=request.session["email"]) # Este es el usuario que manda el mensaje (el que se logueo)
    usuario_destino = Usuario.objects.get(id=user_id) # Este es el usuario que recibe el mensaje (el que pinché)
    if request.method == 'POST':
        # Quiere decir que estamos mandando algún mensaje y tenemos que manejarlo
        if request.POST["type_form"] == "direct_post":
            # Estamos enviando un mensaje al usuario destino
            Mensaje.objects.create(mensaje=request.POST["post"],
                                   usuario_origen=usuario_origen,
                                   usuario_destino=usuario_destino)
    context={
        'usuario_origen': usuario_origen,
        'usuario_destino': usuario_destino,
        'mensajes_recibidos': Mensaje.objects.filter(usuario_destino=usuario_destino)
    }
    return render(request, 'show_user.html', context=context)

def edit_user(request, user_id):
    if request.method == 'POST':
        usuario = Usuario.objects.get(id=user_id)
        if request.POST['type_form'] == 'update':
            # Actualizo registro
            usuario.email = request.POST['email']
            usuario.nombre = request.POST['nombre']
            usuario.apellido = request.POST['apellido']
            usuario.user_level = request.POST['user_level']
            usuario.save()
        elif request.POST['type_form'] == 'pwd':
            # Actualizo contraseña
            if request.POST["password"] == request.POST["conf_password"]:
                passw = request.POST["password"]
                user_hash = bcrypt.hashpw(passw.encode(), bcrypt.gensalt()).decode()
                usuario.password = user_hash
                usuario.save()

    context={
        'user_id': user_id
    }
    return render(request, 'edit_user.html', context=context)

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
    if request.session.get('email') == None:
        return redirect('/signin/')
    if request.method == 'POST':
        usuario = Usuario.objects.get(email=request.session['email'])
        if request.POST['type_form'] == 'update':
            # Actualizo registro de usuario
            usuario.email = request.POST['email']
            usuario.nombre = request.POST['nombre']
            usuario.apellido = request.POST['apellido']
        elif request.POST['type_form'] == 'pwd':
            # Actualizo contraseña
            if request.POST["password"] == request.POST["conf_password"]:
                passw = request.POST["password"]
                user_hash = bcrypt.hashpw(passw.encode(), bcrypt.gensalt()).decode()
                usuario.password = user_hash
        elif request.POST["type_form"] == "desc":
            # Actualización de descripción
            usuario.descripcion = request.POST["description"]

        usuario.save()

    return render(request, 'users_edit.html')
