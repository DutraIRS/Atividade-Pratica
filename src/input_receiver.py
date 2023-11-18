class InputReceiver:
    # Single-responsability: receive input
    # Open-closed: can be extended by InputValidator, but not modified

    def __init__(self, validator: "InputValidator") -> None:
        self._input_received = None
        self.validator = validator

    @property
    def input_received(self):
        return self._input_received
    
    @input_received.setter
    def input_received(self, value: str) -> None:
        self._input_received = value

    def receive_input(self) -> None:
        input_received = input("Digite o CPF: ")

        while not self.validator.validate(input_received):
            print("CPF inválido")
            print("Formato para inserir CPF -", self.validator.expected_format())
            input_received = input("Digite o CPF: ")

        self.input_received = input_received