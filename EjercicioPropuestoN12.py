class Nomina:
    def __init__(self, horas, valor_hora, retencion):
        self.horas = horas
        self.valor_hora = valor_hora
        self.retencion = retencion

    def calcular_salario_bruto(self):
        return self.horas * self.valor_hora

    def calcular_retencion(self):
        return self.calcular_salario_bruto() * self.retencion

    def calcular_salario_neto(self):
        return self.calcular_salario_bruto() - self.calcular_retencion()

    def mostrar_resultados(self):
        print("Salario bruto:", self.calcular_salario_bruto())
        print("Retención:", self.calcular_retencion())
        print("Salario neto:", self.calcular_salario_neto())


horas = 48
valor_hora = 5000
retencion = 0.125

empleado = Nomina(horas, valor_hora, retencion)
empleado.mostrar_resultados()
