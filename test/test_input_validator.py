import sys
sys.path.append('./src')

import input_validator
import unittest

class TestInputValidator(unittest.TestCase):
    """ All tests for the InputValidator class
    """
    def setUp(self):
        """ Set up the test case by instantiating the InputValidator class
        """        
        self.validator = input_validator.InputValidator()

    def test_validate_valid_input(self):
        """ Test InputValidator.validate() with a valid CPF
        """        
        self.assertTrue(self.validator.validate('123.456.789-00'))

    def test_validate_wrong_length(self):
        """ Test InputValidator.validate() with a CPF with the wrong length
        """
        # Test with 12 digits        
        self.assertFalse(self.validator.validate('123.456.789-000'))
        # Test with 10 digits
        self.assertFalse(self.validator.validate('123.456.789-0'))

    def test_validate_missing_punctuation(self):
        """ Test InputValidator.validate() with a CPF with missing punctuation
        """
        # Test with missing hyphens
        self.assertFalse(self.validator.validate('123.456.78900'))
        # Test with missing dots
        self.assertFalse(self.validator.validate('123456.789-00'))
        self.assertFalse(self.validator.validate('123.456789-00'))

    def test_validate_wrong_punctuation(self):
        """ Test InputValidator.validate() with a CPF with wrong punctuation
        """
        # Test with hyphens instead of dots
        self.assertFalse(self.validator.validate('123-456-789-00'))
        # Test with dots instead of hyphens
        self.assertFalse(self.validator.validate('123.456.789.00'))
        # Test with commas instead of dots
        self.assertFalse(self.validator.validate('123,456,789,00'))

    def test_validate_non_digit_characters(self):
        """ Test InputValidator.validate() with a CPF with non-digit characters
        """
        # Test with non digit in each block
        self.assertFalse(self.validator.validate('123.456.789-0X'))
        self.assertFalse(self.validator.validate('123.456.78X-00'))
        self.assertFalse(self.validator.validate('123.45X.789-00'))
        self.assertFalse(self.validator.validate('12X.456.789-00'))

if __name__ == '__main__':
    unittest.main()