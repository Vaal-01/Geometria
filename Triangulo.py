import math
from Punto import Punto


class Triangulo:

  def __init__(self,p1=Punto,p2=Punto,p3=Punto):
    self.p1=p1
    self.p2=p2
    self.p3=p3

  def determinarTipo(self):
        tipo=""
       
        if ((self.p1.calcularDistancia(self.p2))==(self.p2.calcularDistancia(self.p3)) and (self.p2.calcularDistancia(self.p3))==(self.p3.calcularDistancia(self.p1))):
            tipo="Equilatero"
        elif((self.p1.calcularDistancia(self.p2))==(self.p2.calcularDistancia(self.p3)) and (self.p2.calcularDistancia(self.p3))!=(self.p3.calcularDistancia(self.p1))):
            tipo="Isoceles"
        else:
            tipo="Escaleno"
        return tipo
    
  def hallarPerimetro(self):
        perimetroT=(self.p1.calcularDistancia(self.p2))+(self.p2.calcularDistancia(self.p3))+(self.p3.calcularDistancia(self.p1))
        return perimetroT

  def hallarArea(self):
        tipo=self.determinarTipo()
        areaT=0
        if (tipo=="Isoceles"):
            altura=math.sqrt((math.pow((self.p1.calcularDistancia(self.p2)),2))-(math.pow((self.p2.calcularDistancia(self.p3)),2)/4))
            areaT=((self.p2.calcularDistancia(self.p3))*altura)/2
        elif(tipo=="Equilatero"):
            areaT=((self.p1.calcularDistancia(self.p2))*math.pow(3,1/3))/4
        else:
            perimetro=self.hallarPerimetro()/2
            areaT=math.sqrt(perimetro*(perimetro-(self.p1.calcularDistancia(self.p2)))*(perimetro-(self.p2.calcularDistancia(self.p3)))*perimetro-(self.p3.calcularDistancia(self.p1)))
        
        return areaT