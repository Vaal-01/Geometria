import unittest
import Rectangulo

from Punto import Punto
from Rectangulo import Rectangulo


class Test(unittest.TestCase):

    def testHallarArea(self):
         p1=Punto(-1,0)
         p2=Punto(1,0)    
         p3=Punto(-1,1)    
         p4=Punto(1,1)
         r=Rectangulo(p1,p2,p3,p4)
         self.assertEqual(2,r.hallarArea())

    def testHallarPerimetro(self):
         p1=Punto(-1,0)
         p2=Punto(1,0)    
         p3=Punto(-1,1)    
         p4=Punto(1,1)
         r=Rectangulo(p1,p2,p3,p4)
         self.assertEqual(6,r.hallarPerimetro())
        
if __name__ == '__main__':
    unittest.main()