# Cargamos el módulo unittest
import unittest
from src import Calculator

# Creamos una clase heredando de TestCase
class TestMyCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_initial_value(self):
        self.assertEqual(0, self.calc.value)

    def test_add_method(self):
        self.calc.add(1, 3)
        self.assertEqual(4, self.calc.value)

    def test_subtract_method(self):
        self.calc.subtract(8, 2)
        self.assertEqual(6, self.calc.value)

    def test_multiply_method(self):
        self.calc.multiply(2, 3)
        self.assertEqual(6, self.calc.value)

    def test_divide_method(self):
        self.calc.divide(8, 2)
        self.assertEqual(4, self.calc.value)

    def test_power_method(self):
        self.calc.power(2, 3)
        self.assertEqual(8, self.calc.value)

    def test_square_root_method(self):
        self.calc.square_root(9)
        self.assertEqual(3, self.calc.value)

    def test_logarithm_method(self):
        self.calc.logarithm(100, 10)
        self.assertEqual(2, self.calc.value)

    def test_sine_method(self):
        self.calc.sine(90)
        self.assertEqual(1, self.calc.value)

    def test_cosine_method(self):
        self.calc.cosine(0)
        self.assertEqual(1, self.calc.value)

    def test_tangent_method(self):
        self.calc.tangent(45)
        self.assertEqual(1, self.calc.value)

    def test_factorial_method(self):
        self.calc.factorial(5)
        self.assertEqual(120, self.calc.value)