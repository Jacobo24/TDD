import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return math.sqrt(a)

def logaritmo(a, base=10):
    if a <= 0:
        raise ValueError("El logaritmo solo está definido para números positivos")
    return math.log(a, base)

def seno(a):
    return math.sin(math.radians(a))

def coseno(a):
    return math.cos(math.radians(a))

def tangente(a):
    return math.tan(math.radians(a))

def factorial(a):
    if a < 0:
        raise ValueError("No se puede calcular el factorial de un número negativo")
    return math.factorial(a)