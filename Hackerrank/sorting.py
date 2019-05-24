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

A matriz é classificada em swaps numSwaps.
onde está o número de trocas ocorridas.
Primeiro Elemento: firstElement
onde é o primeiro elemento na matriz classificada.
Último elemento: lastElement
onde é o último elemento na matriz classificada.

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

