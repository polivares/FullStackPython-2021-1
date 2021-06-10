class Persona:
    def __init__(self, nombre="", edad=0):
        self.nombre = nombre
        self.edad = edad

    def getName(self):
        return self.nombre
    
    def getAge(self):
        return self.edad

    def showPerson(self):
        return f"Nombre:, {self.nombre}, Edad:, {self.edad}"

class Profesor(Persona):
    def __init__(self, nombre="", edad=0, n_contrato=0):
        Persona.__init__(self, nombre, edad)
        self.n_contrato = n_contrato
    
class Estudiante(Persona):
    def __init__(self, nombre="", edad=0, idEstudiante=0):
        Persona.__init__(self, nombre, edad)
        self.idEstudiante = idEstudiante


class Curso:
    def __init__(self):
        self.lista_curso = []
        self.profesor = ""

    def setProfessor(self, prof):
        self.profesor = prof

    def addStudent(self, std):
        self.lista_curso.append(std)

    def showCurso(self):
        print("El profesor de este curso es:", self.profesor.showPerson())
        print("Los estudiantes de este curso son:")
        for s in self.lista_curso:
            print(s.showPerson())

curso = Curso()

profesor = Profesor("Patricio", 35, 10)

std1 = Estudiante("Juanito", 25, 20)
std2 = Estudiante("Rosa", 27, 30)

curso.setProfessor(profesor)
curso.addStudent(std1)
curso.addStudent(std2)

curso.showCurso()

    