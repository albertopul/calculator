import sys
import unittest

path = r'C:\Users\Albert\Desktop\testy\unittest-kurs\project\calculator'
sys.path.append(path)
from calculator.calc import Calculator

class TestClass(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print('setting up class...')
        cls.calc = Calculator()

    @classmethod
    def tearDownClass(cls):
        print('tearing down class...')
        del cls.calc

    def test_add(self):
        self.assertEqual(Calculator.add(3, 4), 7)

    def test_add_with_one_negative_number(self):
        self.assertEqual(Calculator.add(-5, 4), -1)

    def test_add_with_two_negative_numbers(self):
        self.assertEqual(Calculator.add(-35, -24), -59)

    def test_add_with_zero(self):
        self.assertEqual(Calculator.add(5, 0), 5)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(3, 4), -1)

    def test_subtract_with_one_negative_number(self):
        self.assertEqual(Calculator.subtract(-4, 4), -8)

    def test_subtract_with_zero(self):
        self.assertEqual(Calculator.subtract(43, 0), 43)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(3, 4), 12)
    
    def test_multiply_with_one_negative_number(self):
        self.assertEqual(Calculator.multiply(12, -4), -48)

    def test_multiply_with_zero(self):
        self.assertEqual(Calculator.multiply(5, 0), 0)

    def test_divide(self):
        self.assertEqual(Calculator.divide(6, 2), 3)

    def test_divide_with_one_negative_number(self):
        self.assertEqual(Calculator.divide(-3, 3), -1)

    def test_divide_by_zero_should_raise_error(self):
        self.assertRaises(ZeroDivisionError, Calculator.divide, 43, 0)


if __name__ == '__main__':
    unittest.main()