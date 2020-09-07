### Introducir  una palabra y mostrar primer y ultimo caracter
import unittest

def logica():
    palabra = str(input('Introduzca una palabla '))
    indice = palabra[0]
    longitud=len(palabra)
    ultima=palabra[longitud-1]
    print('el primer y ultimo caracter de la palabra ingresada son: ')
    print (indice, ultima)
    return (indice, ultima )


class PruebasFunciones(unittest.TestCase):
     def test_palabra_primera(self):
        (inicio,final)=logica()
        self.assertEquals('h', inicio)
        self.assertEquals('a',final)
      

if __name__ == "__main__":
    unittest.main()