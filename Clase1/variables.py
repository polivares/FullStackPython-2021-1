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

# Quiero escribir por pantalla: El valor de la variable a1 es <aquí va el valor de a1> y el valor de a2 es <aquí va el valor de a2>
# Ej: El valor de la variable a1 es 10 y el valor de la variable a2 es 15.3
# Formas de hacer esto
print("El valor de la variable a1 es", a1, "y el valor de la variable a2 es", a2)
print("El valor de la variable a1 es " + str(a1) + " y el valor de la variable a2 es " + str(a2))
print("El valor de la variable a1 es %d y el valor de la variable a2 es %f" % (a1, a2))
print(f"El valor de la variable a1 es {a1} y el valor de la variable a2 es {a2}")

