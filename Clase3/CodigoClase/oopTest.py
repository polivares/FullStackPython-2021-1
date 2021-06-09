# Sistema para pruebas de CodingDojo

# Definimos las clases involucradas en nuestro problema
class Curso:
    def __init__(self):
        self.lista_curso = []

    def addStudent(self, student):
        self.lista_curso.append(student)

    def removeLastStudent(self):
        self.lista_curso.pop()

    def showCurso(self):
        for i in self.lista_curso:
            print("Nombre estudiante:", i.getName(), "Edad:", i.getAge())

class Estudiante:
    def __init__(self, nombre="", edad=0):
        self.nombre = nombre
        self.edad = edad

    def getName(self):
        return self.nombre

    def getAge(self):
        return self.edad
    
# Acá utilizamos estas clases creando objetos

# Acá se crea el curso
fullStackPython = Curso()

# Acá se crean los estudiantes
std1 = Estudiante("Juanito", 25)
std2 = Estudiante("Mónica", 30)

# Luego agregamos los estudiantes al curso
fullStackPython.addStudent(std1)
fullStackPython.addStudent(std2)

# Mostramos el curso por pantalla
fullStackPython.showCurso()



