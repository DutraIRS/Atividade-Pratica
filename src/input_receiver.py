from validator import Validator

class InputReceiver:
    """ Single-responsability: Interact with the user

    Open-closed: can be extended by InputValidator, but not modified
    """

    def __init__(self, *validator: [Validator]) -> None:
        """ Class to interact with the user

        :param validator: All validators to be used to validate the input
        :type validator: [Validator]
        """        
        self._input_received = None
        self.validators = validator

    @property
    def input_received(self) -> str:
        """ Getter for the input received

        :return: Input received
        :rtype: str
        """        
        return self._input_received
    
    @input_received.setter
    def input_received(self, value: str) -> None:
        """ Setter for the input received

        :param value: Input received
        :type value: str
        """        
        self._input_received = value

    def receive_input(self) -> None:
        """ Function to interact with the user
        """        
        input_received = input("Digite o CPF: ")

        valid = False
        # Loop until cpf received is valid
        while not valid:
            # Loop through all validators
            for each_validator in self.validators:
                valid = each_validator.validate(input_received)

                if not valid:
                    print("CPF inválido")
                    print("Formato para inserir CPF -", each_validator.expected_format)
                    input_received = input("Digite o CPF: ")
                    break

        self.input_received = input_received
        print("CPF válido, obrigado por oferecer seus dados pessoais!")