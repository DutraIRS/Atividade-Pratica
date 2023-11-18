import sys
sys.path.append('./src')

import input_receiver
import unittest
from unittest.mock import Mock, patch

class TestInputReceiver(unittest.TestCase):
    # Equivalence partitioning: input is either valid or invalid
    # Invalid -> ... -> Invalid -> Valid is the same as Invalid -> Valid
    def setUp(self):
        self.validator = Mock()
        self.receiver = input_receiver.InputReceiver(self.validator)

    @patch('builtins.input', return_value='123.456.789-00')
    def test_receive_input_valid(self, input):
        self.validator.validate.return_value = True
        self.receiver.receive_input()
        self.assertEqual(self.receiver.input_received, '123.456.789-00')

    @patch('builtins.input', side_effect=['invalid', '123.456.789-00'])
    def test_receive_input_invalid_then_valid(self, input):
        self.validator.validate.side_effect = [False, True]
        self.validator.expected_format.return_value = 'XXX.XXX.XXX-XX'
        self.receiver.receive_input()
        self.assertEqual(self.receiver.input_received, '123.456.789-00')

if __name__ == '__main__':
    unittest.main()