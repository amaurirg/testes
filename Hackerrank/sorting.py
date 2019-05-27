"""
Objetivo
Hoje, estamos discutindo um algoritmo de classificação simples chamado Bubble Sort.

Considere a seguinte versão do Bubble Sort:

para (int i = 0; i <n; i ++) {
    // Rastreia o número de elementos trocados durante uma travessia de matriz única
    int numberOfSwaps = 0;
    
    para (int j = 0; j <n - 1; j ++) {
        // Trocar elementos adjacentes se estiverem em ordem decrescente
        if (a [j]> a [j + 1]) {
            swap (a [j], a [j + 1]);
            numberOfSwaps ++;
        }
    }
    
    // Se nenhum elemento foi trocado durante uma travessia, a matriz é classificada
    if (numberOfSwaps == 0) {
        pausa;
    }
}
Tarefa
Dado um array, um, de tamanho n elementos distintos, classifique o array em ordem crescente
usando o algoritmo Bubble Sort acima. Depois de ordenar, imprima as 3 linhas seguintes:

1 - A matriz é classificada em swaps numSwaps.
onde numSwaps é o número de trocas ocorridas.
2 - Primeiro Elemento: firstElement
onde firstElement é o primeiro elemento na matriz classificada.
3 - Último Elemento: lastElement
onde lastElement é o último elemento na matriz classificada.
Dica: Para completar este desafio, você precisará adicionar uma variável que mantenha uma contagem
de todos os swaps que ocorrem durante a execução.

Formato de entrada
A primeira linha contém um inteiro, n, denotando o número de elementos na matriz a.
A segunda linha contém n inteiros separados por espaços descrevendo os respectivos valores de a0, a1, ...., an-1.

Restrições
2 <= n <= 600
1 <= ai <= 2 x 10 ** 6, onde 0 <= i <= n.

Formato de saída
Imprima as três linhas de saída a seguir:

A matriz é classificada em swaps numSwaps onde está o número de trocas ocorridas.
Primeiro Elemento: onde firstElement é o primeiro elemento na matriz classificada.
Último elemento: onde lastElement é o último elemento na matriz classificada.

Entrada de Amostra 0
3
1 2 3

Amostra de Saída 0
Array é classificado em 0 swaps.
Primeiro elemento: 1
Último Elemento: 3

Explicação 0
A matriz já está classificada, então ocorrem 0 trocas e nós imprimimos as 3 linhas de saída necessárias
mostradas acima.

Entrada de amostra 1
3
3 2 1

Exemplo de Saída 1
Array é classificado em 3 swaps.
Primeiro elemento: 1
Último Elemento: 3

Explicação 1
A matriz a = [3, 2, 1] não está classificada, portanto, realizamos as seguintes 3 trocas:
1 - [3, 2, 1] -> [2, 3, 1]
2 - [2, 3, 1] -> [2, 1, 3]
3 - [2, 1, 3] -> [1, 2, 3]

Neste ponto, a matriz é classificada e nós imprimimos as 3 linhas necessárias de saída mostradas acima.
"""

#!/bin/python3

import sys


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
"""
for i in range(n):
    numSwaps = 0
    for j in (n-1):
        if a[j] > a[j + 1]:
            (a[j], a[j + 1])
            numSwaps += 1
"""

def bubble(arr):
    count_swap = 0
    for num in range(len(arr)-1, 0, -1):
        for i in range(num):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                count_swap +=1
    return count_swap

print("Array is sorted in {} swaps.".format(bubble(a)))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))


"""
#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

swaps = 0
is_sorted = False

while not is_sorted:
    is_sorted = True
    i = 0
    for i in range(0, len(a)):
        if i < len(a) - 1:
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                is_sorted = False
                swaps += 1

print('Array is sorted in {} swaps.'.format(swaps))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[len(a)-1]))
"""