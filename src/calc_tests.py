##
# @project IVS Kalkulačka
# @file calc_tests.py
# @brief Testy pre kalkulačku
# @author xlachmd00, David Lachman
##

import sys
import os

# Add the 'src' directory to the system path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import unittest
from calculator import add, subtract, multiply, divide, factorial, power, root, modulo, sin, postfix


class ColorTestResult(unittest.TextTestResult):
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'

    def getDescription(self, test):
        return super().getDescription(test)

    def addSuccess(self, test):
        self.stream.write(self.GREEN)
        super().addSuccess(test)
        self.stream.write(self.RESET)

    def addFailure(self, test, err):
        self.stream.write(self.RED)
        super().addFailure(test, err)
        self.stream.write(self.RESET)

    def addError(self, test, err):
        self.stream.write(self.RED)
        super().addError(test, err)
        self.stream.write(self.RESET)


##
# @class TestMathLibrary
# @brief Sada jednotkových testov pre matematické funkcie kalkulačky.
##
class TestMathLibrary(unittest.TestCase):
    ##
    # @brief Testovanie funkcie sčítania.
    ##
    def test_add(self):
        self.assertEqual(add(7, 8), 15)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(2.5, 4.5), 7.0)
        self.assertEqual(add(0, 10), 10)
        self.assertEqual(add(500000, 300000), 800000)
        self.assertAlmostEqual(add(0.2, 0.3), 0.5, places=7)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)

    ##
    # @brief Testovanie funkcie odčítania.
    ##
    def test_subtract(self):
        self.assertEqual(subtract(8, 5), 3)
        self.assertEqual(subtract(5, 8), -3)
        self.assertEqual(subtract(0, 8), -8)
        self.assertEqual(subtract(-15, -7), -8)
        self.assertEqual(subtract(300000, 100000), 200000)
        self.assertAlmostEqual(subtract(0.5, 0.2), 0.3, places=7)
        self.assertAlmostEqual(subtract(0.2, 0.5), -0.3, places=7)

    ##
    # @brief Testovanie funkcie násobenia.
    ##
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(2.0, 3.5), 7.0)
        self.assertEqual(multiply(0, 10), 0)
        self.assertEqual(multiply(-4, -2), 8)
        self.assertEqual(multiply(100000, 200000), 20000000000)
        self.assertEqual(multiply(0.1, 0.2), 0.02)

    ##
    # @brief Testovanie funkcie delenia.
    ##
    def test_divide(self):
        self.assertEqual(divide(9, 3), 3)
        self.assertRaises(ValueError, divide, 9, 0)
        self.assertAlmostEqual(divide(10, 4), 2.5, places=4)
        self.assertAlmostEqual(divide(8, 2), 4.0, places=4)
        self.assertAlmostEqual(divide(-15, 3), -5)
        self.assertAlmostEqual(divide(0, 5), 0.0, places=4)
        self.assertRaises(ValueError, divide, 0, 0)
        self.assertRaises(ValueError, divide, 0, -1)
        self.assertRaises(ValueError, divide, -1, 0)
        self.assertRaises(ValueError, divide, -1, -1)


    ##
    # @brief Testovanie funkcie faktoriálu.
    ##
    def test_factorial(self):
        self.assertEqual(factorial(6), 720)
        self.assertRaises(ValueError, factorial, -3)
        self.assertRaises(ValueError, factorial, 3.5)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
        self.assertRaises(ValueError, factorial, -1)

    ##
    # @brief Testovanie funkcie umocňovania.
    ##
    def test_power(self):
        self.assertEqual(power(3, 2), 9)
        self.assertEqual(power(7, 0), 1)
        self.assertEqual(power(-3, 3), -27)
        self.assertEqual(power(-4, 2), 16)
        self.assertAlmostEqual(power(2, -2), 0.25)
        self.assertAlmostEqual(power(0, 5), 0)
        self.assertRaises(ValueError, power, 0, -1)
        self.assertRaises(ValueError, power, 0, 0)
        self.assertRaises(ValueError, power, -2, 0.5)
        self.assertRaises(ValueError, power, -2, -0.5)


    ##
    # @brief Testovanie funkcie odmocniny.
    ##
    def test_root(self):
        self.assertEqual(root(16, 2), 4)
        self.assertEqual(root(27, 3), 3)
        self.assertRaises(ValueError, root, -16, 2)
        self.assertAlmostEqual(root(-27, 3), -3)
        self.assertRaises(ValueError, root, 16, 0)
        self.assertRaises(ValueError, root, 16, -2)
        self.assertAlmostEqual(root(0, 2), 0)
        self.assertAlmostEqual(root(1, 2), 1)

    ##
    # @brief Testovanie funkcie modulo (zvyšok po delení).
    ##
    def test_modulo(self):
        self.assertEqual(modulo(14, 5), 4)
        self.assertEqual(modulo(15, 3), 0)
        self.assertRaises(ValueError, modulo, 15, 0)
        self.assertEqual(modulo(-15, 4), -3)
        self.assertEqual(modulo(10, -3), 1)
        self.assertEqual(modulo(-10, -3), -1)

    ##
    # @brief Testovanie funkcie sínus (Taylorova aproximácia).
    ##
    def test_sin(self):
        self.assertAlmostEqual(sin(0), 0.0, places=5)
        self.assertAlmostEqual(sin(30), 0.5, places=2)
        self.assertAlmostEqual(sin(90), 1.0, places=2)
        self.assertAlmostEqual(sin(180), 0.0, places=2)
        self.assertAlmostEqual(sin(270), -1.0, places=2)
        self.assertAlmostEqual(sin(360), 0.0, places=2)
        self.assertAlmostEqual(sin(-90), -1.0, places=2)

        ##
    # @brief Testovanie funkcie konverzie do postfixovej notácie.
    ##
    def test_postfix(self):
        # Príklady: vstupný reťazec -> očakávaný výstup ako zoznam
        self.assertEqual(postfix("3+4"), ['3', '4', '+'])
        self.assertEqual(postfix("3+4*2"), ['3', '4', '2', '*', '+'])
        self.assertEqual(postfix("(1+2)*3"), ['1', '2', '+', '3', '*'])
        self.assertEqual(postfix("7+8*(3-1)"), ['7', '8', '3', '1', '-', '*', '+'])
        self.assertEqual(postfix("5+(6-2)*9+3"), ['5', '6', '2', '-', '9', '*', '+', '3', '+'])
        self.assertEqual(postfix("4+(13/5)"), ['4', '13', '5', '/', '+'])
        self.assertEqual(postfix("2+3*4^2"), ['2', '3', '4', '2', '^', '*', '+'])
        
        # Neplatný vstup
        with self.assertRaises(ValueError):
            postfix("3++4")

        with self.assertRaises(ValueError):
            postfix("2.3.4")

        with self.assertRaises(ValueError):
            postfix("5*/2")

        with self.assertRaises(ValueError):
            postfix("(2+3")


if __name__ == '__main__':
    runner = unittest.TextTestRunner(
        verbosity=2,
        resultclass=ColorTestResult
    )
    runner.run(unittest.defaultTestLoader.loadTestsFromTestCase(TestMathLibrary))
