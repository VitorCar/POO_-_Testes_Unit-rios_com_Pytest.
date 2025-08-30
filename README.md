# Mini Projeto - Funcionários + Testes Unitários com Pytest

Este projeto é um exemplo prático de Programação Orientada a Objetos (POO) em Python com foco em testes unitários utilizando o framework pytest.
A ideia é modelar diferentes tipos de funcionários dentro de uma empresa (Funcionário, Gerente, Estagiário e Diretor), cada um com suas particularidades, e validar o funcionamento do código com testes automatizados.

---

## Tecnologias Utilizadas

- **Python 3+**
- **Pytest** → Framework de testes
- **Pytest-cov** → Plugin do pytest para medir cobertura de testes

---

## Classes Implementadas

- **Funcionario** → Classe base com nome e salário.  
- **Gerente** → Herda de Funcionario e adiciona o departamento.  
- **Estagiario** → Herda de Funcionario e adiciona departamento + horas trabalhadas.  
- **Diretor** → Herda de Funcionario e adiciona horas trabalhadas + participação nos lucros.  

Cada classe possui o método `exibir()`, que mostra os dados formatados.

---

## Testes com Pytest

O projeto contém testes automatizados para garantir que o código funcione corretamente.

## Executando os testes

No terminal, execute:

- **pytest -v**

Instalando o pytest-cov.
No terminal, execute:

- **pip install pytest-cov**

Para verificar o percentual de cobertura de testes na sua aplicação.
No terminal, execute:

- **pytest test.py --cov -v**

Também pode usar o coverage para gerar uma página web co relatorio completo dos testes.
No terminal, execute:

- **coverage html**

---

## O que você vai aprender com este projeto?

- Criar classes em Python utilizando herança e encapsulamento
- Organizar código seguindo os princípios de POO
- Escrever testes unitários com pytest
- Utilizar pytest-cov para medir cobertura
- Estruturar um mini-projeto Python para estudo e prática

---

## Referências

- Documentação oficial do pytest
- Documentação do pytest-cov
- Python Classes e POO

---

## Autor: Vitor Carvalho Sant Ana

## Projeto feito com fins didáticos para iniciantes em Python, POO e Testes Unitários.
