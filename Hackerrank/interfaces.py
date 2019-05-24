"""
Objetivo
Hoje estamos aprendendo sobre Interfaces.

Tarefa
A interface AdvancedArithmetic e a declaração de método para o método abstrato divisorSum (n)
são fornecidas para você no editor abaixo.

Conclua a implementação da classe Calculator, que implementa a interface AdvancedArithmetic.
A implementação para o método divisorSum (n) deve retornar a soma de todos os divisores de n.

Formato de entrada
Uma única linha contendo um inteiro, n.

Restrições
1 <= n <= 1000

Formato de saída
Você não é responsável por imprimir nada no stdout. O código de modelo bloqueado no editor abaixo
irá chamar seu código e imprimir a saída necessária.

Entrada de amostra
6

Saída de Amostra
Eu implementei: AdvancedArithmetic
12

Explicação
O inteiro 6 é divisível por 1, 2, 3 e 6. Nosso método divisorSum deve retornar a soma desses números,
que é 1 + 2 + 3 + 6 = 12. A classe Solution então imprime eu implantei: AdvancedArithmetic na
primeira linha, seguida pela soma retornada por divisorSum (que é 12) na segunda linha.
"""

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        return sum([num for num in range(1, n+1) if n % num == 0])


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
