### Introducir un numero por teclado y decir si es par o impar
import unittest

def operacion():
    num = int(input('Introduzca un numero: '))
    if num % 2 == 0:
        print('Par')
        return 1
    else:
        print('Impar')
        return 0

def es_par(a): return 1 if a%2 == 0 else 0

class PruebasFunciones(unittest.TestCase):
    def test_es_par(self):
        self.assertEqual(es_par(10), operacion())

if __name__ == "__main__":
    unittest.main()