"""
Objetivo
Hoje estamos aprendendo sobre o tempo de execução!

Tarefa
Um primo é um número natural maior que 1 que não possui divisores positivos além de 1 e ele próprio.
Dado um número, n, determine e imprima se é Prime ou Not prime.
Nota: Se possível, tente criar um algoritmo de primalidade 0 (^ N) ou veja que tipo de otimizações
você usa para um algoritmo 0 (n). Não deixe de conferir o Editorial depois de enviar seu código!

Formato de entrada
A primeira linha contém um inteiro, T, o número de casos de teste.
Cada uma das linhas subsequentes T contém um inteiro, n, para ser testado para primalidade.

Restrições
1 <= T <= 1000
1 <= n <= 2 x 10 ** 9

Formato de saída
Para cada caso de teste, imprima se n é Prime ou Not prime em uma nova linha.

Entrada de amostra
3
12
5
7

Saída de Amostra
Not prime
Prime
Prime

Explicação
Caso de Teste 0: n = 12.
12 é divisível por números diferentes de 1 e ele próprio (ou seja, 2, 3, 6), por isso imprimimos
Not prime em uma nova linha.

Caso de Teste 1: n = 5.
5 é apenas divisível 1 e ele, então imprimimos Prime em uma nova linha.

Caso de Teste 2: n = 7.
7 é somente divisível 1 e ele mesmo, então imprimimos Prime em uma nova linha.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

def isprime(n):
    if n == 1:
        return 'Not prime'
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return 'Not prime'
    return 'Prime'

T = int(input())
for i in range(T):
    number = int(input())
    print(isprime(number))