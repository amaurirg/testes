"""
Objetivo
Hoje, estamos construindo nosso conhecimento de matrizes adicionando outra dimensão.

Contexto
Dado um array 6x6 2D, A:
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

Definimos uma ampulheta em A para ser um subconjunto de valores com índices que caem neste
padrão na representação gráfica A's:

a b c
  d
e f g

Há 16 ampulhetas em A, e uma soma de ampulheta é a soma dos valores de uma ampulheta.

Tarefa
Calcule a soma da ampulheta para cada ampulheta em A e imprima a soma máxima da ampulheta.

Formato de entrada
Existem 6 linhas de entrada, onde cada linha contém 6 números inteiros separados por espaços
descrevendo a matriz A 2D; cada valor em A será na faixa inclusiva de -9 para 9.

Restrições
-> -9 <= A[i][j] <= 9
-> 0 <= i,j  <= 5

Formato de saída
Imprima a maior (máxima) quantia de ampulheta encontrada em A.

Entrada de amostra
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output
19

Explicação
A contém as seguintes ampulhetas:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0

A ampulheta com a soma máxima (19) é:
2 4 4
  2
1 2 4

"""


# if name == 'main':
#
arr = []

for row in range(6):
    arr.append(list(map(int, input().rstrip().split())))

hourglass = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        try:
            hourglass.append(sum([arr[i][j],
                          arr[i][j+1],
                          arr[i][j+2],
                          arr[i+1][j+1],
                          arr[i+2][j],
                          arr[i+2][j+1],
                          arr[i+2][j+2]]))
        except IndexError as e:
            continue
print(max(hourglass))


# res = []
#
# for x in range(0, 4):
#     for y in range(0, 4):
#         s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
#         res.append(s)
#
# print(max(res))