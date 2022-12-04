"""Crear una clase llamada Punto con sus coordenadas X e Y.

Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.

Añade un método llamado cuadrante que indique a que cuadrante pertenece el punto, teniendo en cuenta que:

Si x==0 e Y !=0 se sitúa sobre el eje Y, si x!=0 e Y==0 se sitúa sobre el eje X y si X==0 esta sobre el origen.

Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos."""

from math import sqrt
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def calcularVector(p1, p2):
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

punto1 = Punto(3,2)
punto2 = Punto(-3,-5)

print(calcularVector(punto1, punto2))
