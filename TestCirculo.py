import unittest
import math
import Circulo
import Punto

from Circulo import Circulo
from Punto import Punto


class Test(unittest.TestCase):

    def testPerimetro(self):
         p1=Punto(0,0)
         c=Circulo(3,p1)
         self.assertEqual(6*math.pi,c.hallarPerimetro())

    def testArea(self):
         p1=Punto(0,0)
         c2=Circulo(3,p1)
         self.assertEqual(9*math.pi,c2.hallarArea())

    def testdeterminarDentro(self):
         p1=Punto(0,0)
         c3=Circulo(3,p1)
         p2=Punto(1,2)
         self.assertEqual(True,c3.determinarDentro(p2))
   

if __name__ == '__main__':
    unittest.main()