# importar el marco de prueba de Python 
import unittest

# nuestra "unit"
# esto es lo que estamos ejecutando nuestra prueba en 
def isEven(n):
    if n % 2 == 0:
       return True
    else:
       return False


# nuestros "unit tests" 
# inicializado creando una clase que hereda de unittest.TestCase 
class IsEvenTests(unittest.TestCase):
    # cada método en esta clase es una prueba que se ejecutará 
    def testTwo(self):
        self.assertEqual(isEven(2), True)
        # otra forma de escribir arriba es 
        self.assertTrue(isEven(2))
    def testThree(self):
        self.assertEqual(isEven(3), False)
        # otra forma de escribir lo de arriba es
        self.assertFalse(isEven(3))
    #  cualquier tarea que desee ejecutar antes de ejecutar cualquier método anterior, colóquelas en el método setUp 
    def setUp(self):
        # agrega las tareas setUp 
        print("running setUp")
    # cualquier tarea que quieras ejecutar después de ejecutar las pruebas, ponlas en el método
    def tearDown(self):
        # agrega las tareas tearDown 
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # esto ejecuta nuestras pruebas