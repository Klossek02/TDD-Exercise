import unittest
from string_calculator import StringCalculator

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
        string = '15,4'
        expected_result = 19
        # when
        result = StringCalculator.calculate(string)
        # then
        self.assertEqual(result, expected_result)

    # two numbers, newline delimited, returns the sum
    def test_two_numbers_newline(self):
        # given
        string = '7\n7'
        expected_result = 14
        # when 
        result = StringCalculator.calculate(string)
        # then
        self.assertEqual(result, expected_result)
    
    # three numbers, delimited either way, returns the sum
    def test_three_numbers(self):
        # given 
        string = '14,8,6'
        expected_result = 28
        # when
        result = StringCalculator.calculate(string)
        # then
        self.assertEqual(result, expected_result)

    # negative numbers throw an exception
    def test_negative_numbers(self):
        # given 
        string = '-7'
        # then
        self.assertRaises(Exception, StringCalculator.calculate, string)

    
    # numbers greater than 1000 are ignored
    def test_ignore_greater_1000(self):
        # given
        string = '1000,3333,222'
        expected_result = 222
        # when
        result = StringCalculator.calculate(string)
        # then
        self.assertEqual(result, expected_result)

    # a single char delimiter can be defined on the first line 
    def test_single_char_delimiter(self):
        # given
        string = '//#\n4#5#2'
        expected_result = 11
        # when
        result = StringCalculator.calculate(string)
        # then
        self.assertEqual(result, expected_result)
    
    # a multi char delimiter can be defined on the first line
    def test_mult_char_delimiter(self):
        # given 
        string = '//[***]\n10***4***5'
        expected_result = 19
        # when
        result = StringCalculator.calculate(string)
        # then
        self.assertEqual(result, expected_result)

    # many single or multi-char delimiters can be defined
    def test_single_multi_char_delimiter(self):
        # given
        string = '//[*][%]\n1*2%3'
        expected_result = 6
        # when 
        result = StringCalculator.calculate(string)
        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
