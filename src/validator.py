from abc import ABC, abstractmethod

class Validator(ABC):
    def __init__(self, expected_format: str = "XXX.XXX.XXX-XX") -> None:
        self._expected_format = expected_format

    @abstractmethod    
    def validate(self, input):
        ...
    
    @property
    def expected_format(self):
        return self._expected_format
    
    @expected_format.setter
    def expected_format(self, value: str) -> None:
        self._expected_format = value