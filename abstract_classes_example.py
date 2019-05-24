"""
Objetivo
Hoje, estamos pegando o que aprendemos ontem sobre Herança e estendendo-o para o Abstract Classes.
Como esse é um conceito orientado a objetos muito específico, as submissões estão limitadas aos poucos
idiomas que usam essa construção.

Tarefa
Dada uma classe Book e uma classe Solution, escreva uma classe MyBook que faça o seguinte:

Herda de livro
Tem um construtor parametrizado, tomando estes 3 parâmetros:
string title
string author
int price

Implementa o método abstract display () da classe Book para que imprima estas 3 linhas:
Título, um espaço e, em seguida, a instância atual.
Autor, um espaço e, em seguida, a instância atual.
Preço, um espaço e, em seguida, o da instância atual.

Nota: Como essas classes estão sendo gravadas no mesmo arquivo, você não deve usar um modificador de
acesso (por exemplo, public) ao declarar MyBook ou seu código não será executado.

Formato de entrada
Você não é responsável por ler qualquer entrada de stdin. A classe Solution cria um objeto Book e chama
o construtor de classe MyBook (passando os argumentos necessários). Em seguida, chama o método de
exibição no objeto Book.

Formato de saída
O método void display () deve imprimir e rotular o respectivo título, autor e preço da instância do
objeto MyBook (com cada valor em sua própria linha) da seguinte forma:

Título: $ title
Autor: $ author
Preço: $ preço
Nota: O $ é prefixado aos nomes das variáveis ​​para indicar que eles são espaços reservados para variáveis.

Entrada de amostra
A seguinte entrada do stdin é manipulada pelo código stub bloqueado no seu editor:

O Alquimista
Paulo Coelho
248
Saída de Amostra

A seguinte saída é impressa pelo seu método display ():
Título: O Alquimista
Autor: Paulo Coelho
Preço: 248
"""

class Funcionario:

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    # outros métodos e propriedades
    def get_bonificacao(self):
        return self._salario * 0.10


class Gerente(Funcionario):

    def __init__(self, nome, cpf, salario, senha, qtd_funcionarios):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios

    def autentica(self, senha):
        if self._senha == senha:
            print("acesso permitido")
            return True
        else:
           print("acesso negado")
           return False

    # outros métodos (comuns a um Funcionario)
    def get_bonificacao(self):
        return super().get_bonificacao() + 1000

    def __str__(self):
        return '< Instância de {}; endereço:{}>'.format(self.__class__.__name__, id(self))


class ControleDeBonificacoes:

    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes

    def registra(self, obj):
        if(hasattr(obj, 'get_bonificacao')):
            self._total_bonificacoes += obj.get_bonificacao()
        else:
            print('instância de {} não implementa o método get_bonificacao()'.format(self.__class__.__name__))

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes


class Cliente:

    def __init__(self, nome, cpf, senha):
        self._nome = nome
        self._cpf = cpf
        self._senha = senha


# if __name__ == '__main__':
    # funcionario = Funcionario('João', '111111111-11', 2000.0)
    # print("bonificacao funcionario: {}".format(funcionario.get_bonificacao()))
    #
    # gerente = Gerente("José", "222222222-22", 5000.0, '1234', 0)
    # print("bonificacao gerente: {}".format(gerente.get_bonificacao()))
    #
    # controle = ControleDeBonificacoes()
    # controle.registra(funcionario)
    # controle.registra(gerente)
    #
    # print("total: {}".format(controle.total_bonificacoes))
    #
    # cliente = ('Maria', '333333333-33', '1234')
    # controle = ControleDeBonificacoes()
    # controle.registra(cliente)


"""
class Ponto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Ponto({}, {})".format(self.x + 1, self.y + 1)

if __name__ == '__main__':
    p1 = Ponto(1, 2)
    p2 = eval(repr(p1))

    print(p1)
    print(p2)
"""