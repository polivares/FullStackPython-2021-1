# Este comentario solo llega hasta acá 
''' Este es un comentario de múltiples
líneas y puede llegar


hasta acá
'''
x = 2 # Esta es la variable x
y = 5 # Esta es la variable y
z = x + y # En z se almacena el resultado de x + y
print(z)

a1 = 10 # Este es un número entero (int)
a2 = 15.3 # Este es un número con decimales (float)
a3 = "Este es un text" # Este es un string (str)
a4 = True # Este es un valor booleano (bool)
a5 = 3.3 + 5.1j # Este es un número complejo (complex)

print(a1, a2, a3, a4, a5)

# Quiero escribir por pantalla: El valor de la variable a1 es <aquí va el valor de a1> 
# y el valor de a2 es <aquí va el valor de a2>
# Ej: El valor de la variable a1 es 10 y el valor de la variable a2 es 15.3
# Formas de hacer esto
print("El valor de la variable a1 es", a1, "y el valor de la variable a2 es", a2)
print("El valor de la variable a1 es " + str(a1) + " y el valor de la variable a2 es " + str(a2))
print("El valor de la variable a1 es %d y el valor de la variable a2 es %f" % (a1, a2))
print(f"El valor de la variable a1 es {a1} y el valor de la variable a2 es {a2}")

# Tipos de datos compuestos
# Existen 3 tipos: listas, tuplas, y los diccionarios
# Listas
lista1 = [ 1, 2, 3]
lista2 = ["texto1", "texto2"]
lista3 = [1, "texto", True, 4+5.3j, [1,10,3]]
print("Listas creadas:", lista1, lista2, lista3)
p = lista1[1]
print("El valor de p es: ", p)
q = lista3[4][1]
print("El valor de q es:", q)
lista1.append(4)
print("Lista1 actualizada:", lista1)
lista1.pop()
print("Lista1 luego de pop:", lista1)
lista1 = lista1[0:1] + lista1[2:] 
print("Resultado de concatenar y actualizar lista1:", lista1)

# Tuplas: igual que las listas pero inmutables!!
tupla1 = (1, 2, 3, "texto", (4,5,6), [7, 8, 9])
print("La tupla1 tiene los siguientes elementos:", tupla1)
print("El elemento en la posición índice 2 de la tupla1 es", tupla1[1])
print("Los 3 primeros elementos de la tupla1 son:", tupla1[0:3])

# Diccionarios: tipo de dato compuesto cuyo acceso se puede dar con índices de distinto tipo
# Requisito para los índices: deben ser INMUTABLES
dict1 = {
    0: "Texto para indice 0",
    "key1": "Texto para la llave key1",
    (1,2,3): "Texto para la llave tupla (1,2,3)"
}

print("El diccionario dict1 es:", dict1)
dict1["nuevoIndice"] = "Este es el texto del nuevo índice"
print("El nuevo valor del diccionario dict1 es:", dict1)

print("Acceso a key1 en dict1 es ", dict1["key1"])

# Inicialización de múltiples variables al mismo tiempo
a1, a2, a3, a4, a5 = 3, "hola", True, "chao", (1,2,3)
print("Variables recién creadas", a1, a2, a3, a4, a5)

# Type, len y funciones de tipo
x = 3
y = float(x)
print("Esta es la variable x pero convertida en flotante y asignada a y", y)

tupla2 = (1, 2, 3)
lista_tupla2 = list(tupla2)
print("La variable lista_tupla2 es ", lista_tupla2)

r = "hola"
# Se me olvidó de que tipo de dato era la variable r. ¿Cómo puedo saberlo ahora?
print("El tipo de la variable r es", type(r))

# ¿Cómo saber cuál es el largo de la lista_tupla2?
print("El largo de lista_tupla2 es", len(lista_tupla2))