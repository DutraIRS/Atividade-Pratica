import sys
sys.path.append('./src')

import input_receiver
import unittest
from unittest.mock import Mock, patch

class TestInputReceiver(unittest.TestCase):
    """ All tests for the InputReceiver class
    """
    def setUp(self):
        """ Set up the test case by instantiating the InputReceiver class
        """
        # Mock the validator class, so that we can control its behavior        
        self.validator = Mock()
        self.receiver = input_receiver.InputReceiver(self.validator)

    @patch('builtins.input', return_value='123.456.789-00')
    def test_receive_input_valid(self, input):
        """ Test InputReceiver.receive_input() with a valid CPF
        """
        # Mock the validator's behavior to validate the input as True
        self.validator.validate.return_value = True
        self.receiver.receive_input()
        self.assertEqual(self.receiver.input_received, '123.456.789-00')

    @patch('builtins.input', side_effect=['invalid', '123.456.789-00'])
    def test_receive_input_invalid_then_valid(self, input):
        """ Test InputReceiver.receive_input() with an invalid CPF followed by
            a valid one
        """
        # Mock the validator's behavior to validate the input as False, then
        # True
        self.validator.validate.side_effect = [False, True]
        self.validator.expected_format.return_value = 'XXX.XXX.XXX-XX'
        self.receiver.receive_input()
        self.assertEqual(self.receiver.input_received, '123.456.789-00')

if __name__ == '__main__':
    unittest.main()