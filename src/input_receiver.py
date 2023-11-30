from validator import Validator

class InputReceiver:
    # Single-responsability: receive input
    # Open-closed: can be extended by InputValidator, but not modified

    def __init__(self, *validator: [Validator]) -> None:
        self._input_received = None
        self.validators = validator

    @property
    def input_received(self):
        return self._input_received
    
    @input_received.setter
    def input_received(self, value: str) -> None:
        self._input_received = value

    def receive_input(self) -> None:
        input_received = input("Digite o CPF: ")

        valid = False
        while not valid:
            for each_validator in self.validators:
                valid = each_validator.validate(input_received)

                if not valid:
                    print("CPF inválido")
                    print("Formato para inserir CPF -", self.validator.expected_format())
                    input_received = input("Digite o CPF: ")
                    break

        self.input_received = input_received