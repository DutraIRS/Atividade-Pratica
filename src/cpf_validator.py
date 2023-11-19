import numpy as np

class CPFValidator:
    # Single-responsability: validate CPF
    # Open-closed: can be extended by subclasses that override the validate method,
        # without modifying the original class.
    def __init__(self) -> None:
        pass
    
    def validate_CPF(self, cpf: str) -> bool:
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
