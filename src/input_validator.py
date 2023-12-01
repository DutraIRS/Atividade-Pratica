from validator import Validator

class InputValidator(Validator):
    """ Single-responsability: Validate input string

    Open-closed: can be extended by subclasses that override the validate method,
        without modifying the original class.
    """       
    def validate(self, input: str) -> bool:
        """ Validates the input format according to the following rules:
            - Input must have 14 characters
            - Input must have points and dashes in the correct positions
            - Input must have digits in the correct positions

        :param input: String to be validated
        :type input: str
        :return: True if input is valid, False otherwise
        :rtype: bool
        """
        # Check if input has 14 characters       
        if len(input) != 14:
            return False
        # Check if input has points and dashes in the correct positions
        if input[3] + input[7] + input[11] != "..-":
            return False
        # Check if input has digits in the correct positions
        if not (input[0:3] + input[4:7] + input[8:11] + input[12:14]).isdigit():
            return False
        
        return True