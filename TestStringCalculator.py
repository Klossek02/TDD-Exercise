import unittest
from StringCalculator import StringCalculator

class CalculatorTest(unittest.TestCase):
    # an empty string returns zero
    def test_returns_zero(self):
        # given 
        string = ''
        expected_result = 0 
        # when
        result = StringCalculator.calculate(string)  
        # then 
        self.assertEqual(result, expected_result)  
    

    # a single number returns the value
    def test_single_number(self):
        # given
        string = '22'
        expected_result = 22 
        # when
        result = StringCalculator.calculate(string)  
        # then
        self.assertEqual(result, expected_result)  


    # two numbers, comma delimited, returns the sum

    def test_two_numbers_comma(self):
        # given 
        string = "15,4"
        expected_result = 19
        # when
        result = StringCalculator.calculate(string)
        # then
        self.assertEqual(result, expected_result)


    # negative numbers throw an expection 

    def test_negative_numbers(self):
        # given
        string = '-7'
        # then
        self.assertRaises(Exception, StringCalculator.calculate, string)

if __name__ == '__main__':
    unittest.main()