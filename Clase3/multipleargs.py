# Puedes agregar múltiples argumentos a las funciones y de distintas maneras
def f1(a,b,c):
    print(a,b,c)

f1(1,2,3)
f1(b=1,c=2,a=3)

# Formas de indicar argumentos de entrada

def f2(a, b,*args):
    print(a,b)
    for i in args:
        print(i)

print("Función llamada con dos argumentos")
f2(1,2) # Esto muestra los dos primeros parámetros solamente
print("Función llamada con cuatro argumentos")
f2(1,2,3,4)
print("Función llamada con ocho argumentos")
f2(1,2,3,4,5,6,7,8)


# ¿Qué ocurre si necesito agregar parámetros asociados a un elemento en particular?

def f3(**kwargs):
    print(kwargs["a"])
    for i in kwargs.items():
        print(i[0], i[1])
    
    
print("Llamando función con 3 parámetros de entrada como diccionarios de valores")
f3(a=1, b=2, c=3)
print("Llamando función con 2 parámetros de entrada como diccionarios de valores")
f3(primero=1, segundo=2)

