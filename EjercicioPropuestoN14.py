import math

class Potencias:
    def __init__(self, numero):
        self.numero = numero

    def calcular_cuadrado(self):
        return math.pow(self.numero , 2)

    def calcular_cubo(self):
        return math.pow(self.numero , 3)

    def mostrar_resultados(self):
        print("Cuadrado:", self.calcular_cuadrado())
        print("Cubo:", self.calcular_cubo())


n = int(input("Ingrese un número: "))

potencia = Potencias(n)
potencia.mostrar_resultados()
