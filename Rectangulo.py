from Punto import Punto
class Rectangulo:
  def __init__(self,p1=Punto,p2=Punto,p3=Punto,p4=Punto):
   self.p1=p1
   self.p2=p2
   self.p3=p3
   self.p4=p4

  def hallarPerimetro(self):
         perimetro=(self.p1.hallarDistancia(self.p2))+(self.p2.hallarDistancia(self.p4))+(self.p3.hallarDistancia(self.p1))+(self.p4.hallarDistancia(self.p3))
         return perimetro
    

  def hallarArea(self):
         area=(self.p1.hallarDistancia(self.p2))*(self.p2.hallarDistancia(self.p4))
         return area