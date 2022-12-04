"""Crea una clase llamada Rectángulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.

Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.

Añade al rectángulo un método llamado base que muestre la base.

Añade al rectángulo un método llamado altura que muestre la altura.

Añade al rectángulo un método llamado área que muestre el área."""

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        resultado = self.ancho * self.alto
        return resultado

    def perimetro(self):
        resultado = 2 * (self.ancho + self.alto)
        return resultado

r = Rectangulo(10, 7)
print("el area del rectangulo: " + r.area)
print("el perimetro del rectangulo: " + r.perimetro)