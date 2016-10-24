"""
Run unittest tests: $ python3 -m unittest
Run pytest tests:   $ pytest

"""

from string_calculator import StringCalculator

# import unittest

# class StringCalculatorTest(unittest.TestCase):

#     def setUp(self):
#         self.calculator = StringCalculator()

#     def test_add_empty_string(self):
#         result = self.calculator.add('')
#         self.assertEqual(0, result)

import pytest

@pytest.fixture
def calculator():
    return StringCalculator()

def test_add_empty_string(calculator):
    result = calculator.add('')
    assert 0 == result

def test_add_single_number(calculator):
    result = calculator.add('1')
    assert 1 == result

def test_add_two_numbers(calculator):
    result = calculator.add('1,2')
    assert 3 == result

def test_add_multiple_numbers(calculator):
    result = calculator.add('1,2,3,4,5')
    assert 15 == result

def test_add_handles_newlines(calculator):
    result = calculator.add("1\n2,3")
    assert 6 == result

def test_add_with_provided_delimiter(calculator):
    result = calculator.add("//;\n1;2")
    assert 3 == result
