import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * math.pow(self.radio , 2)

    def calcular_longitud(self):
        return 2 * math.pi * self.radio

    def mostrar_resultados(self):
        print("Área del círculo:", self.calcular_area())
        print("Longitud de la circunferencia:", self.calcular_longitud())


r = float(input("Ingrese el radio: "))

circulo = Circulo(r)
circulo.mostrar_resultados()
