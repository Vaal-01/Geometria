import unittest
import Punto

from Punto import Punto

class Test(unittest.TestCase):
    def calcularDistancia(self):
         p1=Punto(2,0)
         p2=Punto(-3,0)
         d=int(p1.calcularDistancia(p2))
         self.assertEqual(5,d) 
        

if __name__ == '__main__':
    unittest.main()
