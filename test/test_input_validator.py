import sys
sys.path.append('./src')

import input_validator
import unittest

class TestInputValidator(unittest.TestCase):
    # Equivalence partitioning: invalid inputs can be divided into:
    #   - wrong length
    #   - missing punctuation
    #   - wrong punctuation
    #   - non-digit characters
    def setUp(self):
        self.validator = input_validator.InputValidator()

    def test_validate_valid_input(self):
        self.assertTrue(self.validator.validate('123.456.789-00'))

    def test_validate_wrong_length(self):
        self.assertFalse(self.validator.validate('123.456.789-000'))
        self.assertFalse(self.validator.validate('123.456.789-0'))

    def test_validate_missing_punctuation(self):
        self.assertFalse(self.validator.validate('123.456.78900'))
        self.assertFalse(self.validator.validate('123456.789-00'))
        self.assertFalse(self.validator.validate('123.456789-00'))

    def test_validate_wrong_punctuation(self):
        self.assertFalse(self.validator.validate('123-456-789-00'))
        self.assertFalse(self.validator.validate('123.456.789.00'))
        self.assertFalse(self.validator.validate('123,456,789,00'))

    def test_validate_non_digit_characters(self):
        self.assertFalse(self.validator.validate('123.456.789-0X'))
        self.assertFalse(self.validator.validate('123.456.78X-00'))
        self.assertFalse(self.validator.validate('123.45X.789-00'))
        self.assertFalse(self.validator.validate('12X.456.789-00'))

if __name__ == '__main__':
    unittest.main()