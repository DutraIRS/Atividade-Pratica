class InputValidator:
    # Single-responsability: validate input
    # Open-closed: can be extended by subclasses that override the validate method,
        # without modifying the original class.

    def __init__(self, expected_format: str = "XXX.XXX.XXX-XX") -> None:
        self._expected_format = expected_format
        
    def validate(self, input):
        if len(input) != 14:
            return False
        if input[3] + input[7] + input[11] != "..-":
            return False
        if not (input[0:3] + input[4:7] + input[8:11] + input[12:14]).isdigit():
            return False
        
        return True
    
    @property
    def expected_format(self):
        return self._expected_format
    
    @expected_format.setter
    def expected_format(self, value: str) -> None:
        self._expected_format = value