# Conversiones de tipo. Las conversiones puede ser:
# Explícitas: Se indica explícitamente los tipos involucrados en la conversión
a = "Hola" + str(42)
print("El valor de la variable a es:", a)

# Implícitas: Python se encarga en este caso de determinar el tipo a convertir
b = 42 + 2.5
print("El valor de b es", b, "y su tipo es", type(b))

# Condicionales, bucles y funciones
###################################

# Condiciones: if, elif, else
x = 3

if x < 4:
    print("El valor de x es menor que 4")
    print("Este es otro print dentro de esta condición")
elif x <8:
    print("El valor de x es menor que 8")
elif x < 20:
    print("El valor de x es menor que 20")
else:
    print("El valor de x no cumple las condiciones")

# Bucles: 
# Existen dos tipos de bucles: for y while

# For
lista1 = [[7,4,2],[8,1,9]]

# Por cada i en lista1... hago algo
for i in lista1:
    print(i[0])

for i in lista1:
    print("Iterando...")
    # En i hay una lista... que también puedo recorrer!!
    # Por cada elemento j en la lista i (porque i es una lista ahora)... hago algo
    for j in i:
        print(j)

# ¿Puedo recorrer arreglos como lo hacía en Javascript? ¿Con un índice?
# R: Por supuesto!

lista2 = [1,2,8, 7, 3, 1]
print("Recorriendo lista2 con índices")
for i in range(0,len(lista2),1):
    print(lista2[i])

# While (Mientras)
k = 1
# Mientras k sea menor que 10... hago algo
while k <10:
    if k%3 == 0:
        k += 1
        print("Entré al continue")
        continue

    if k%4 == 0:
        print("Entré al break")
        break
    print("El valor de k es:", k)
    k = k + 1 # k += 1 
else:
    print("Ya se terminaron las iteraciones")

print("Fuera del ciclo while")

# Funciones: Bloques de códigos que pueden ser llamados desde otro
def sumaN(p):
    return sum(range(p))

print("La suma de los 10 primeros naturales (sin contar el 10) es:", sumaN(10))

# Las funciones pueden tener 0, 1 o muuuuchos parámetros

def getMessage():
    return "Este es mi mensaje"

print("El mensaje es:", getMessage())

def sumaNumeros(a, b):
    return a+b

print("La suma de a y b es", sumaNumeros(3,8))

# Las funciones en python, permiten parámetros por omisión!!

def sumaTresNumeros(a, b, c=0):
    return a+b+c

print("La suma de a, b y c es:", sumaTresNumeros(5, 2))

# Nos falta un operador condicional... el único operador ternario de python!!
a = 7
# Es como un if. Si a es igual a 5, devuelvo un 2 (que recibe la variable b )
# Sino, devuelvo un 4 (que también recibe la variable b)
b = 2 if a==5 else 4

print("El valor de b es:", b)

# Programación Orientada a Objetos en Python
# Definición de clases

class MiPrimeraClase:
    def __init__(self):
        self.a = 10
        self.b = "hola"
        self.c = [1,2,3]

    def getA(self):
        return self.a

objeto = MiPrimeraClase()
print("El valor de a como atributo de objeto es:",objeto.a)
print("El valor de a desde el método de clase del objeto es:",objeto.getA())

# Ejemplo: una clase persona
class Persona:
    def __init__(self, rut1, edad1, nombre1="Pedro"):
        self.rut = rut1
        self.edad = edad1
        self.nombre = nombre1
        self.miprimerObjeto = MiPrimeraClase()
        
    def dameTuNombre(self):
        return self.nombre

p = Persona("11111111-1", 20)
print("El nombre de la persona p es", p.nombre)

# Puedes crear listas de objetos!!
listaPersonas = [Persona("11111111-1",20, "Juan"), Persona("2222222-2",40)]
print("El nombre de la primera persona es:", listaPersonas[0].dameTuNombre())

# Tambien puedes acceder a los atributos y metodos de variables internas
# definidas como objetos de una clase!!
print("El atributo a definido en el objeto dentro de la primera Persona es:", listaPersonas[0].miprimerObjeto.a)
