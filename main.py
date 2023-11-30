import sys
sys.path.append('./src')

from cpf_validator import CPFValidator
from input_validator import InputValidator
from input_receiver import InputReceiver

validador_de_input = InputValidator()
validador_de_cpf = CPFValidator()
system = InputReceiver(validador_de_input, validador_de_cpf)

if __name__ == '__main__':
    system.receive_input()