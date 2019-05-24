"""
Objetivo
Hoje, estamos trabalhando com números binários.

Tarefa
Dado um inteiro base-10, n, converta-o em binário (base-2). Em seguida, encontrar e imprimir o base-10
inteiro denotando o número máximo de consecutivos 1's em n's representação binária.

Formato de entrada

Um único inteiro, n.

Restrições
- 1 <= n <= 10^6

Formato de saída
Imprime um único inteiro base-10 denotando o número máximo de consecutivos 1's na representação binária de n.

Entrada de amostra 1
5

Exemplo de Saída 1
1

Entrada de Amostra 2
13

Exemplo de Saída 2
2
Explicação

Caso de exemplo 1:
A representação binária de 5 é 101 , portanto, o número máximo de consecutivos 1's é 1.

Exemplo de Caso 2:
A representação binária de 13 é 1101 , portanto, o número máximo de consecutivos 1's é 2.
"""

def convert_decimal_to_binary(number):
    return format(number, 'b')


def count_numbers_1(result):
    return max(result.split('0')).count('1')

try:
    n = int(input())

    result = convert_decimal_to_binary(n)
    max_consecutive_numbers_1 = count_numbers_1(result)

    print(max_consecutive_numbers_1)
except:
    pass