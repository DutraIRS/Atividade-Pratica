# Atividade-Pratica
 Atividade de Qualidade de Software para a disciplina de Engenharia de Software. O objetivo da atividade é refatorar o código presente no arquivo `original_code.py` dividindo-o em classes, respeitando as boas práticas de OO e os princípios de Single Responsability e Open-Closed.

 Após refatoração do código (presente agora na pasta `.\src`), foi confeccionada uma suíte de testes (presente na pasta `.\test`) que, como pedido, cobre 90% do código desenvolvido.

# Participantes
- Ana Julia Lima
- George Dutra
- Iago Riveiro Santos Dutra
- Luan Rodrigues de Carvalho
- Luís Henrique Domingues Bueno

# Cobertura de Testes

Para verificar a cobertura de testes, foi realizado o teste padrão do `coverage.py` seguindo os seguintes passos:
- Instale o módulo com a linha de comando:

        pip install coverage

- Na pasta raiz do repositório, rode as seguintes linhas de comando para processar os testes:

        coverage run -a .\test\test_cpf_validator.py
        coverage run -a .\test\test_input_validator.py
        coverage run -a .\test\test_input_receiver.py

- Por fim, gere um report em terminal com o comando:

        coverage report

    Ou para melhor visualização, rode o comando:

        coverage html

    E abra o arquivo `index.html` que será gerado no diretório `.\htmlcov`