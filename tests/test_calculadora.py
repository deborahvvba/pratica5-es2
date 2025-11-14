import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculadora()
    
    def test_somar(self):
        self.assertEqual(self.calc.somar(5, 3), 8)
        self.assertEqual(self.calc.somar(-1, 1), 0)
    
    def test_subtrair(self):
        self.assertEqual(self.calc.subtrair(10, 5), 5)
        self.assertEqual(self.calc.subtrair(5, 10), -5)
    
    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(4, 3), 12)
        self.assertEqual(self.calc.multiplicar(7, 0), 0)
    
    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)
        self.assertEqual(self.calc.dividir(5, 2), 2.5)
    
    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)
    
    def test_potencia(self):
        self.assertEqual(self.calc.potencia(2, 3), 8)
        self.assertEqual(self.calc.potencia(5, 0), 1)

if __name__ == '__main__':
    unittest.main()
