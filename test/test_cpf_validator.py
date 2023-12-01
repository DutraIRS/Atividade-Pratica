import sys
sys.path.append('./src')

import cpf_validator
import unittest

class TestCPFValidator(unittest.TestCase):
    """ All tests for the CPFValidator class
    """    
    def setUp(self) -> None:
        """ Set up the test case by instantiating the CPFValidator class
        """
        self.validator = cpf_validator.CPFValidator()
    
    def test_validate_CPF_valid_CPF(self) -> None:
        """ Test CPFValidator.validate() with a valid CPF
        """        
        self.assertTrue(self.validator.validate('123.456.789-09'))
    
    def test_validate_CPF_all_digits_equal(self) -> None:
        """ Test CPFValidator.validate() with CPFs where all digits are equal,
            for all digits from 0 to 9
        """
        for i in range(10):
            cpf_all_equal = f"{i}{i}{i}.{i}{i}{i}.{i}{i}{i}-{i}{i}"
            self.assertFalse(self.validator.validate(cpf_all_equal))
    
    def test_validate_CPF_first_verifier_digit_wrong(self) -> None:
        """ Test CPFValidator.validate() with CPFs where the first verifier
            digit is wrong, for all digits from 1 to 9
        """
        for i in range(1, 10):
            self.assertFalse(self.validator.validate(f"123.456.789-{i}9"))
    
    def test_validate_CPF_second_verifier_digit_wrong(self) -> None:
        """ Test CPFValidator.validate() with CPFs where the second verifier
            digit is wrong, for all digits from 1 to 9
        """        
        for i in range(1, 9):
            self.assertFalse(self.validator.validate(f"123.456.789-0{i}"))

if __name__ == '__main__':
    unittest.main()
