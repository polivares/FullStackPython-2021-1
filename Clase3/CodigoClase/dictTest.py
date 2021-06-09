# Recorramos el diccionario!
listDict = [
    {"id": 1567, "nombre": "Pepe"},
    {"id": 2214, "nombre": "Juan"},
    {"id": 5724, "nombre": "Alberto" }
]

for i in listDict:
    print(i)

dictTest = {"id": 1567, "nombre": "Pepe"}
# Recorrer diccionario a partir de sus llaves
for i in dictTest.keys():
    print(i)

# Recorrer diccionario a partir de los valores asociados a cada llave
for i in dictTest.values():
    print(i)

# Recorrer todos los elementos del diccionario (llave, valor)
for i in dictTest.items():
    print(i)


# Recorriendo una lista de diccionarios
for i in listDict:
    salida=""
    for j in i.keys():
        salida += f"{j} - {i[j]} " # Estoy mostrando primero la llave del diccionario (variable j) y luego el valor del diccionario en la posición con llave j (i[j])

    print(salida)

# Por supuesto, lo podemos hacer de manera directa si sabemos de antemano los valores de las llaves
for i in listDict:
    print("id -", i["id"], " - nombre - ", i["nombre"] )