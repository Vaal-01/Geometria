import math

from Punto import Punto

class Circulo():

  def __init__(self,radio,punto):
   self.punto = punto
   self.radio = radio

   
  def hallarPerimetro(self):
        perimetroC=(2*math.pi*self.radio)
        return perimetroC
    

  def hallarArea(self):
        areaC=(math.pi*math.pow(self.radio,2))
        return areaC
    
  def determinarDentro(self,otro):

        if (self.punto.calcularDistancia(otro))<=self.radio:
            val=True
        else:
            val=False

        return val