import unittest
from src.calculator import Calculator

# Creamos una clase heredando de TestCase
class TestMyCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_initial_value(self):
        self.assertEqual(0, self.calc.value)

    def test_suma(self):
        self.assertEqual(3, self.calc.suma(1, 2))
        self.assertEqual(5, self.calc.suma(2, 3))
    
    def test_resta(self):
        self.assertEqual(-1, self.calc.resta(1, 2))
        self.assertEqual(-1, self.calc.resta(2, 3))
    
    def test_multiplicacion(self):
        self.assertEqual(2, self.calc.multiplicacion(1, 2))
        self.assertEqual(6, self.calc.multiplicacion(2, 3))
    
    def test_division(self):
        self.assertEqual(0.5, self.calc.division(1, 2))
        self.assertEqual(1, self.calc.division(2, 2))
        self.assertEqual("Error: division entre cero", self.calc.division(1, 0))
    
    def test_potencia(self):
        self.assertEqual(1, self.calc.potencia(1, 2))
        self.assertEqual(8, self.calc.potencia(2, 3))
    
    def test_factorial(self):
        self.assertEqual(1, self.calc.factorial(0))
        self.assertEqual(1, self.calc.factorial(1))
        self.assertEqual(2, self.calc.factorial(2))
        self.assertEqual("Error: factorial de un número negativo", self.calc.factorial(-4))