import unittest
import Triangulo
import math

from Triangulo import Triangulo
from Punto import Punto


class Test(unittest.TestCase):
    def testDeterminarTipo(self):
         p1=Punto(0,0)
         p2=Punto(4,0)    
         p3=Punto(3,2) 
         t=Triangulo(p1,p2,p3)  
         self.assertEqual("Escaleno",t.determinarTipo())

    def testPerimetro(self):
         p1=Punto(0,0)
         p2=Punto(4,0)    
         p3=Punto(3,2) 
         t=Triangulo(p1,p2,p3)  
         self.assertEqual(9.84161925296378,t.hallarPerimetro())

    def testArea(self):
         p1=Punto(0,0)
         p2=Punto(4,0)    
         p3=Punto(3,2) 
         t=Triangulo(p1,p2,p3) 
         self.assertEqual(4.000000000000001,t.hallarArea())
        
if __name__ == '__main__':
    unittest.main()