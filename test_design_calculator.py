import unittest
from design_calculator import Calculator

class TestCalculate(unittest.TestCase):
    def testcase1(self):
        expression = "2+3+3"
        expected = 8
        cal = Calculator()
        actual = cal.calculate(expression)
        print(actual)
        self.assertEqual(actual, expected)
    
    def testcase2(self):
        expression = "2+3-3"
        expected = 2
        cal = Calculator()
        actual = cal.calculate(expression)
        print(actual)
        self.assertEqual(actual, expected)
    
    def testcase3(self):
        expression = "5/2-3"
        expected = -0.5
        cal = Calculator()
        actual = cal.calculate(expression)
        print(actual)
        self.assertEqual(actual, expected)

if __name__ == '__main__': 
    unittest.main()     