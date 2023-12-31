import numpy as np
from validator import Validator

class CPFValidator(Validator):
    """ Single-responsability: validate CPF

    Open-closed: Can be extended by subclasses that override the validate method,
        without modifying the original class.
    """
    def validate(self, cpf: str) -> bool:
        """ Validates the CPF number according to the following rules:
            - CPF must have 11 digits
            - CPF must have only digits
            - CPF must not have all digits equal
            - CPF first verifier digit must be valid
            - CPF second verifier digit must be valid

        :param cpf: CPF number
        :type cpf: str
        :return: True if CPF is valid, False otherwise
        :rtype: bool
        """
        # Check if all CPF digits are numeric       
        cpf_digits = [int(digit) for digit in cpf if digit.isnumeric()]

        # Check if CPF has all digits equal
        if len(set(cpf_digits)) == 1:
            return False

        # Calculate first verifier digit
        first_nine_digits = np.array(cpf_digits[0:9], dtype=int)
        weights_1 = np.array(range(1, 10), dtype=int)
        verifier_digit_1 = np.dot(first_nine_digits, weights_1) % 11 % 10

        # Calculate second verifier digit
        first_ten_digits = np.concatenate((first_nine_digits, [verifier_digit_1]))
        weights_2 = np.array(range(0, 10), dtype=int)
        verifier_digit_2 = np.dot(first_ten_digits, weights_2) % 11 % 10
        
        calculated_digits = [verifier_digit_1, verifier_digit_2]
        
        return calculated_digits == cpf_digits[9:11]
