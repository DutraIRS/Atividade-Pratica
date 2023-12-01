from abc import ABC, abstractmethod

class Validator(ABC):
    def __init__(self, expected_format: str = "XXX.XXX.XXX-XX") -> None:
        """ Abstract class to validate input format

        :param expected_format: Expected format to be validate,
          defaults to "XXX.XXX.XXX-XX"
        :type expected_format: str, optional
        """        
        self._expected_format = expected_format

    @abstractmethod    
    def validate(self, input: str) -> bool:
        """ Function to validate the expected format of the input

        :param input: String to be validated
        :type input: str
        :return: True if input is valid, False otherwise
        :rtype: bool
        """        
        ...
    
    @property
    def expected_format(self) -> str:
        """ Getter for the expected format of the input

        :return: Expected format of the input
        :rtype: str
        """        
        return self._expected_format
    
    @expected_format.setter
    def expected_format(self, value: str) -> None:
        """ Setter for the expected format of the input

        :param value: Expected format of the input
        :type value: str
        """        
        self._expected_format = value