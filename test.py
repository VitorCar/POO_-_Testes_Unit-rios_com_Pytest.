from main import Funcionario, Gerente, Estagiario, Diretor

def test_funcionario_entrada_dado():
    nome = 'Carlos'
    salario = 2500

    funcionario = Funcionario(
        nome=nome,
        salario=salario
    )

    assert funcionario.nome == nome
    assert funcionario.salario == salario

def test_funcionario_setter_value():
    value = 2500

    funcionario = Funcionario(
        nome='Carlos',
        salario=0.0
    )

    funcionario.salario = value

    assert funcionario.salario == value

def test_funcionario_exibir():
    nome = 'Carlos'
    salario = 2500

    funcionario = Funcionario(
        nome=nome,
        salario=salario
    )

    funcionario.exibir()

def test_funcionario_str():
    nome = 'Carlos'

    funcionario = Funcionario(
        nome=nome,
        salario=0.0
    )

    str(funcionario)
    assert funcionario.nome == nome

def test_gerente_entrada_dado():
    nome = 'João'
    salario = 5000
    departamento = 'TI'

    gerente = Gerente(
        nome=nome,
        salario=salario,
        departamento=departamento
    )

    assert gerente.nome == nome
    assert gerente.salario == salario
    assert gerente.departamento == departamento

def test_gerente_exibir():
    nome = 'João'
    salario = 5000
    departamento = 'TI'

    gerente = Gerente(
        nome=nome,
        salario=salario, 
        departamento=departamento
    )

    gerente.exibir()

def test_estagiario_entrada_dado():
    nome = 'Lucas'
    salario = 1200
    departamento = 'Contabilidade'
    horas = 4

    estagiario = Estagiario(
        nome=nome,
        salario=salario,
        departamento=departamento,
        horas_trabalhadas_dia=horas
    )

    assert estagiario.nome == nome
    assert estagiario.salario == salario
    assert estagiario.departamento == departamento
    assert estagiario.horas_trabalhadas_dia == horas

def test_estagiario_exibir():
    nome = 'Lucas'
    salario = 1200
    departamento = 'Contabilidade'
    horas = 4

    estagiario = Estagiario(
        nome=nome,
        salario=salario,
        departamento=departamento,
        horas_trabalhadas_dia=horas
    )

    estagiario.exibir()

def test_diretor_entrada_dado():
    nome = 'Jose'
    salario = 8000
    departamento = 'Diretor Financeiro'
    horas = 7
    porcentagem = 10

    diretor = Diretor(
        nome=nome,
        salario=salario,
        departamento=departamento,
        horas_trabalhadas_dia=horas,
        porcentagem_lucro_empresa=porcentagem
    )

    assert diretor.nome == nome
    assert diretor.salario == salario
    assert diretor.departamento == departamento
    assert diretor.horas_trabalhadas_dia == horas
    assert diretor.porcentagem_lucro_empresa == porcentagem

def test_diretor_exibir():
    nome = 'Jose'
    salario = 8000
    departamento = 'Diretor Financeiro'
    horas = 7
    porcentagem = 10

    diretor = Diretor(
        nome=nome,
        salario=salario,
        departamento=departamento,
        horas_trabalhadas_dia=horas,
        porcentagem_lucro_empresa=porcentagem
    )

    diretor.exibir()
