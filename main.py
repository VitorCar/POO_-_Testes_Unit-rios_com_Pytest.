class Funcionario:
    
    def __init__(self, nome: str, salario: float):
        self.nome = nome 
        self.__salario = salario 

    @property
    def salario(self):
        return self.__salario 
    
    @salario.setter
    def salario(self, value: float):
        self.__salario = value

    def exibir(self):
        print(f'Nome = {self.nome}\nSalário = R${self.__salario:.2f}')

    def __str__(self):
        return f'{self.__class__.__name__}: {self.nome}'
    
class Gerente(Funcionario):
    
    def __init__(self, nome: str, salario: float, departamento: str):
        super().__init__(nome, salario)
        self.departamento = departamento

    def exibir(self):
        super().exibir()
        print(f'Departamento = {self.departamento}')

class Estagiario(Funcionario):

    def __init__(self, nome: str, salario: float, departamento: str, horas_trabalhadas_dia: int):
        super().__init__(nome, salario)
        self.departamento = departamento 
        self.horas_trabalhadas_dia = horas_trabalhadas_dia

    def exibir(self):
        super().exibir()
        print(f'Departamento = {self.departamento}\nHoras trabalhadas = {self.horas_trabalhadas_dia} Horas diárias')

class Diretor(Funcionario):
    
    def __init__(self, nome: str, salario: float, departamento: str, horas_trabalhadas_dia: float, porcentagem_lucro_empresa: float):
        super().__init__(nome, salario)
        self.departamento = departamento
        self.horas_trabalhadas_dia = horas_trabalhadas_dia
        self.porcentagem_lucro_empresa = porcentagem_lucro_empresa

    def exibir(self):
        super().exibir()
        base_salario = self.salario
        soma = base_salario + (base_salario * (self.porcentagem_lucro_empresa / 100))
        porcentagem = (base_salario * (self.porcentagem_lucro_empresa / 100))
        print(f'Departamento = {self.departamento}\nHoras trabalhadas = {self.horas_trabalhadas_dia} Horas diárias')
        print(f'Participação no lucro da empresa = {self.porcentagem_lucro_empresa} -> R${porcentagem:.2f}')
        print(f'Reajuste Salario = R${soma:.2f}')


gerente_1 = Gerente('Carlos', 3400, 'TI')

estagiario_1 = Estagiario('João', 1200, 'Contabilidade', 4)

diretor_1 = Diretor('Jose', 8000, 'Diretor Financeiro', 7, 10)

empresa = [gerente_1, estagiario_1, diretor_1]

for funcionario in empresa:
    print(funcionario)
    funcionario.exibir()
    print('-' * 36)
