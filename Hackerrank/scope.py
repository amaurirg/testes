"""
Objetivo
Hoje estamos discutindo o escopo.

A diferença absoluta entre dois inteiros, a e b, é escrita como | a - b |.
A diferença absoluta máxima entre dois inteiros em um conjunto de inteiros positivos,
é a maior diferença absoluta entre quaisquer dois inteiros em elementos.

A classe Diferença é iniciada para você no editor. Ela tem uma matriz de inteiros privados (elementos)
para armazenar N inteiros não negativos e um inteiro público (maximumDifference) para armazenar a
diferença absoluta máxima.

Tarefa
Complete a classe Diferença escrevendo o seguinte:

Um construtor de classe que usa uma matriz de números inteiros como um parâmetro e salva-a na
variável de instância de elementos.
Um método computeDifference que localiza a diferença absoluta máxima entre quaisquer 2 números em N
e os armazena na variável de ocorrência maximumDifference.

Formato de entrada
Você não é responsável por ler qualquer entrada de stdin. A classe Solution bloqueada no seu editor
lê em 2 linhas de entrada; a primeira linha contém N e a segunda linha descreve os elementos da matriz.

Restrições
1 <= N <= 10
1 <= elementos [i] <= 100, onde 0 <= i <= N - 1

Formato de saída
Você não é responsável por imprimir qualquer saída; a classe Solution imprimirá o valor da variável
da instância.

Entrada de amostra
3
1 2 5

Saída de Amostra
4
Explicação

O escopo da matriz de elementos e o inteiro maximumDifference é toda a instância da classe. O
construtor de classe salva o argumento passado para o construtor como a variável de instância de
elementos (onde o método computeDifference pode acessá-lo).

Para encontrar a diferença máxima, computeDifference verifica cada elemento na matriz e encontra a
diferença máxima entre quaisquer 2 elementos: | 1 - 2 | = 1
| 1 - 5 | = 4
| 2 - 5 | = 3

O máximo dessas diferenças é 4, portanto, ele salva o valor 4 como a variável de ocorrência
maximumDifference. O código stub bloqueado no editor, em seguida, imprime o valor armazenado como
maximumDifference, que é 4.
"""

class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        self.maximumDifference = min(a) - max(a)
        if self.maximumDifference < 0:
            self.maximumDifference *= -1
        return self.maximumDifference

# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]
print(a)
d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
