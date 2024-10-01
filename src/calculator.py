
class Calculator:
    def __init__(self):
        self.value = 0
    
    def suma(self, a, b):
        self.value = a + b
        return self.value
    def resta(self, a, b):
        self.value = a - b
        return self.value
    def multiplicacion(self, a, b):
        self.value = a * b
        return self.value
    def division(self, a, b):
        if b == 0:
            return "Error: division entre cero"
        self.value = a / b
        return self.value
    def potencia(self, a, b):
        self.value = a ** b
        return self.value
    def factorial(self, a):
        self.value = 1
        if a < 0:
            return "Error: factorial de un número negativo"
        for i in range(1, a+1):
            self.value *= i
        return self.value