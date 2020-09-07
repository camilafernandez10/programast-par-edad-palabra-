### Introducir  su edad por teclado y decir la futura edad en el 2070
import unittest

def logica():
    num = int(input('Introduzca su edad: '))
    numFuturo= num+50
    print('su edad en el 2070 sera: ')
    print(numFuturo)
    return numFuturo
def edad(a,b): return a+b  

class PruebasFunciones(unittest.TestCase):
     def test_edad(self):
        b=50
        self.assertEquals(edad(45,b), logica())

if __name__ == "__main__":
    unittest.main()