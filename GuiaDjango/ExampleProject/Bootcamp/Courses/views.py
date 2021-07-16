from django.shortcuts import render, HttpResponse, redirect
from Courses.models import *

# Create your views here.

def index(request):
    # Acá escribiremos el código de la vista index
    return render(request,'index.html')


# Esta función tiene la siguiente responsabilidad
# Va a recibir el registro del formulario, y lo va a almacenar en la base de datos
def register(request):
    #context = {}
    if request.method == 'POST':

        if request.POST.get('type_user') == 'professor':
            # Hacemos registro en la tabla de profesor
            prof = Professor.objects.create(first_name=request.POST["first_name"],
                                            last_name=request.POST["last_name"],
                                            email=request.POST["email"],
                                            password=request.POST["password"])

        elif request.POST.get('type_user') == 'student':
            # Hacemos registro en la tabla de estudiante
            student = Student.objects.create(first_name=request.POST["first_name"],
                                            last_name=request.POST["last_name"],
                                            email=request.POST["email"],
                                            password=request.POST["password"])
                                            
        # Acá haremos los registros en la base de datos
        # y luego podemos hacer un redirect
        # Llenaremos la variable de contexto con un mensaje indicando que se realizó el registro 
        # correctamente

    return redirect('/')

# Encargada de hacer verificación de login
def login(request):
    if request.method == 'POST':
        # Acá verificamos si el usuario es de tipo profesor. 
        # Supuesto: cada profesor/estudiante tiene asociado un único correo
        prof = Professor.objects.filter(email=request.POST["email"])
        if len(prof) == 1:
            # En este punto, me aseguro de que existe un ÚNICO registro con el correo indicado en la tabla
            # de profesores. Por lo tanto, debemos verificar que la contraseña ingresada sea la correcta
            if request.POST['password'] == prof[0].password:
                # Antes del redirect, crearemos una variable de sesión. En este caso, usaremos el email como 
                # información a almacenar en una variable de sesión.
                request.session['email'] = request.POST["email"]
                # Para facilidad de codificación, adicionalmente crearemos una variable de sessión indicando
                # qué tipo de usuario esta logueado
                request.session['type_user'] = "professor"
                # Con el profesor ya verificado, lo redirigimos a la vista de profesor
                return redirect('/professor/')
        
        stud = Student.objects.filter(email=request.POST["email"])
        if len(stud) == 1:
            # En este punto, me aseguro de que existe un ÚNICO registro con el correo indicado en la tabla
            # de estudiantes. Por lo tanto, debemos verificar que la contraseña ingresada sea la correcta
            if request.POST['password'] == stud[0].password:
                # Antes del redirect, crearemos una variable de sesión. En este caso, usaremos el email como 
                # información a almacenar en una variable de sesión.
                request.session['email'] = request.POST["email"]
                # Para facilidad de codificación, adicionalmente crearemos una variable de sessión indicando
                # qué tipo de usuario esta logueado
                request.session['type_user'] = "student"
                # Con el estudiante ya verificado, lo redirigimos a la vista de estudiante
                return redirect('/student/')

    return redirect('/')

# Encargada del borrar las variables de sesión y redirigir al usuario a la vista inicial (de login)
def logout(request):
    if request.method == 'GET':
        # Borraremos las variables de sesión creadas (si es que están creadas)
        request.session.flush()

    return redirect('/')


def professor(request):
    # Primero, vamos a preguntar si alguna de las variables de sesión ha sido creada. Si alguna de estas variables
    # de sesión existe, esto quiere decir que alguien "está logueado" y la sesión de ese usuario está activa.
    if request.session.get('email') != None:
        # Se crean variables email y type_user para facilidad en la codificación y acceso a dichos contenidos
        email = request.session['email']
        type_user = request.session['type_user']
        prof = Professor.objects.get(email=email)
        # En este punto consultaremos todos los cursos disponibles. Estos se encuentran la tabla Courses de la BD.
        cursos = Course.objects.all() # Acá se van a almacenar todos los registros de la tabla de cursos en formato LISTA
        context = {
            'cursos': cursos,
            'name': f'{prof.first_name} {prof.last_name}',
        }
        return render(request, 'professor.html', context=context)
    # En caso contrario, quiere decir que alguien está intentando acceder a esta vista SIN HABERSE LOGUEADO.
    # Por lo tanto, se redirigirá a ese usuario a la página de login para que pueda loguearse
    else:
        return redirect('/')

def create_course(request):
    # Utilizar la variable de sesión type_user (que creamos anteriormente en la vista login), tiene
    # doble funcionalidad:
    # 1) Verificar que una sesión existe. Cada vez que se crea una variable de sesión es porque se ha
    #    creado una sesión. Ojo, en la primera parte no se usa request.session['type_user], porque esta
    #    notación da error si no existe la variable
    # 2) Una vez verificada la existencia de la variable de sesión type_user, preguntaremos por el 
    # tipo de usuario almacenado en esta variable
    if request.session.get('type_user') != None and request.session['type_user'] ==  "professor":
        # Vamos a identificar dos tipos de peticiones sobre la misma vista
        # Petición GET: La petición de tipo GET solo se llama cuando accedemos a la vista
        # Petición POST: La petición POST se llama solo cuando estamos creando un nuevo curso
        if request.method == 'POST':
            # Agregamos registro a la tabla de cursos en la BD
            cod_course = request.POST["cod_course"]
            course_name = request.POST["course_name"]
            max_students = request.POST["max_students"]
            Course.objects.create(cod_course=cod_course,
                                course_name=course_name,
                                max_students=max_students)
        # Creación del contexto. Solo necesitamos el nombre del profesor, por lo que solo se realiza esa
        # consulta
        email = request.session['email']
        prof = Professor.objects.get(email=email)
        context = {
            'name': f'{prof.first_name} {prof.last_name}',
        }
        
        # Y una vez agregado el registro, ya podemos mostrar la página renderizada de la
        # vista correspondiente
        return render(request, 'create_course.html', context=context)
    # En caso de no cumplirse las condiciones de sesión, enviar a la página de inicio
    else:
        return redirect('/')


def student(request):
    # La vista de estudiante está encargada de dos tareas:
    # 1) Mostrar el listado de cursos en los cuales está inscrito un cierto estudiante
    # 2) Permitir, dentro de la lista de cursos disponibles, que un usuario se pueda inscribir 
    #    en un curso  
    
    email = request.session["email"]
    # En este punto tenemos la información del estudiante que ingreso a nuestra página
    student = Student.objects.get(email=email)
    # Ahora, nos falta saber en qué cursos está inscrito nuestro estudiante...
    # Podríamos consultar directamente en la BD... pero el ORM ya nos ayuda en esta tarea!!!
    
    # Creación de variable de contexto
    context = {
        'cursos': [], # En cada posición de esta lista inicialmente vacía, irá la información de cada curso (como una lista)
    }

    ''' Ejemplo de la variable de contexto con datos para esta vista. Supongamos que el estudiante está inscrito en tres cursos
    context = {
        'cursos': [[12246, "Primer curso", 10, 30],
                   [12124, "Segundo curso", 25, 30],
                   [54126, "Tercer curso", 5, 10]  ]

    }

    '''

    # ACÁ TENGO LA INFORMACIÓN DE LOS CURSOS EN LOS CUALES ESTÁ INSCRITO EL ESTUDIANTE
    cursos = student.courses.all()
    # Obtenemos el número de cursos a los cuales el estudiante está inscrito
    n_cursos = len(cursos)
    for curso in cursos:
        # Obtendremos la lista de estudiantes de ese curso y calculamos cuántos hay
        n_students = len(curso.students.all())
        context['cursos'].append({'cod_course': curso.cod_course,
                                  'course_name': curso.course_name,
                                  'n_students': n_students,
                                  'max_students': curso.max_students})
        #context['cursos'].append([curso.cod_course, curso.course_name, 
        #                             n_students, curso.max_students])
                                    


    return render(request, 'student.html', context=context)

