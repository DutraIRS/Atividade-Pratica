import sys
sys.path.append('./src')

import cpf_validator
import unittest

class TestCPFValidator(unittest.TestCase):
    # Assumptions:
    #   - CPF input is already validated
    # Equivalence partitioning: invalid CPFs can be divided into:
    #   - first verifier digit is wrong
    #   - second verifier digit is wrong
    def setUp(self) -> None:
        self.validator = cpf_validator.CPFValidator()
    
    def test_validate_CPF_valid_CPF(self) -> None:
        self.assertTrue(self.validator.validate_CPF('123.456.789-09'))
    
    def test_validate_CPF_first_verifier_digit_wrong(self) -> None:
        for i in range(1, 10):
            self.assertFalse(self.validator.validate_CPF(f'123.456.789-{i}9'))
    
    def test_validate_CPF_second_verifier_digit_wrong(self) -> None:
        for i in range(1, 9):
            self.assertFalse(self.validator.validate_CPF(f'123.456.789-0{i}'))

if __name__ == '__main__':
    unittest.main()
