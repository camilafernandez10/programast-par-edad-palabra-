### Introducir un intervalo por teclado y un numero que se encuentre dentro del rango
import unittest
def logica():
    print ('ingrese los datos, tenga en cuenta que el valor inicial del intervalo debe ser menor al segundo valor')
    i1 = int(input('Introduzca el primer numero del intervalo : '))
    i2=int(input('Introduzca el segundo numero del intervalo : '))
    x=int(input('Introduzca el valor que desea calcular: '))
    cont =0
    c=0
    if x > i1 and x < i2:
        print ('valor valido') 
    if i1<i2:
        while cont <=i2:
            cont += 1
            m=x*cont
            if m>=i1 and m<=i2:
                c+=1
                print ('multiplos de x')
                print (m)
               
        print ('cantidad de multiplos: ')
        print (c)
        print ('intervalo valido')
        return c
    

class PruebasFunciones(unittest.TestCase):
     def test_multiplos(self):
        self.assertEquals(7, logica())

if __name__ == "__main__":
    unittest.main() 