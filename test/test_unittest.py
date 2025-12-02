import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import calculator


class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(calculator.fun1(2, 3), 5)
        self.assertEqual(calculator.fun1(5, 0), 5)
        
        self.assertEqual(calculator.fun1(-1, 1), 0)
        self.assertEqual(calculator.fun1(-1, -1), -2)

    def test_fun2(self):
        self.assertEqual(calculator.fun2(2, 3), -1)
        self.assertEqual(calculator.fun2(5, 0), 5)
        self.assertEqual(calculator.fun2(-1, 1), -2)
        self.assertEqual(calculator.fun2(-1, -1), 0)

    def test_fun3(self):
        self.assertEqual(calculator.fun3(2, 3), 6)
        self.assertEqual(calculator.fun3(5, 0), 0)
        self.assertEqual(calculator.fun3(-1, 1), -1)
        self.assertEqual(calculator.fun3(-1, -1), 1)

    def test_fun4(self):
        self.assertEqual(calculator.fun4(2, 3, 5), 10)
        self.assertEqual(calculator.fun4(5, 0, -1), 4)
        self.assertEqual(calculator.fun4(-1, -1, -1), -3)
        self.assertEqual(calculator.fun4(-1, -1, 100), 98)

    def test_fun5(self):
        self.assertEqual(calculator.fun5(10, 2), 5.0)
        self.assertEqual(calculator.fun5(15, 3), 5.0)
        self.assertEqual(calculator.fun5(-10, 2), -5.0)

    def test_fun5_zero_division(self):
        with self.assertRaises(ValueError):
            calculator.fun5(10, 0)

    def test_fun6(self):
        self.assertEqual(calculator.fun6(2, 3), 8)
        self.assertEqual(calculator.fun6(5, 2), 25)
        self.assertEqual(calculator.fun6(10, 0), 1)
        self.assertEqual(calculator.fun6(2, -1), 0.5)

    def test_fun7(self):
        self.assertEqual(calculator.fun7(10, 3), 1)
        self.assertEqual(calculator.fun7(15, 4), 3)
        self.assertEqual(calculator.fun7(20, 5), 0)

    def test_fun7_zero_division(self):
        with self.assertRaises(ValueError):
            calculator.fun7(10, 0)

    def test_average(self):
        self.assertEqual(calculator.average([2, 4, 6]), 4.0)
        self.assertEqual(calculator.average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(calculator.average([10]), 10.0)

    def test_variance(self):
        result = calculator.variance([1, 2, 3, 4, 5])
        self.assertEqual(result, 2.0)

    def test_standard_deviation(self):
        result = calculator.standard_deviation([1, 2, 3, 4, 5])
        self.assertAlmostEqual(result, 1.414213, places=3)



if __name__ == '__main__':
    unittest.main()