# Usando packages
import fundamentos

p = fundamentos.Persona("11111111-1", 20)
print("El rut de la persona p llamada desde fundamentos.py es:", p.rut)


# Otra forma de importa elementos
from fundamentos import MiPrimeraClase

p2 = MiPrimeraClase()
print(p2.getA())