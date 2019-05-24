import abc


class Funcionario(abc.ABC):

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    @abc.abstractmethod
    def get_bonificacao(self):
        pass
# Agora, se tentarmos instanciar um objeto do tipo Funcionario:


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

    # outros métodos e propriedades
    def get_bonificacao(self):
        return self._salario * 0.15

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


# class Diretor(Funcionario):
#     def __init__(self, nome, cpf, salario):
#         super().__init__(nome, cpf, salario)

# if __name__ == '__main__':
#     diretor = Diretor('joao', '111111111-11', 4000.0)



# if __name__ == '__main__':
#     gerente = Gerente('jose', '222222222-22', 5000.0, '1234', 0)
#     print(gerente.get_bonificacao())



# if __name__ == '__main__':
#     f = Funcionario()