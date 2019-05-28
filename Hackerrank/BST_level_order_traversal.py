"""
Objetivo
Hoje, estamos indo mais longe com as árvores de pesquisa binária.

Tarefa
Uma passagem de ordem de nível, também conhecida como pesquisa de amplitude, visita cada nível dos
nós de uma árvore da esquerda para a direita, de cima para baixo. Você recebe um ponteiro, root,
apontando para a raiz de uma árvore de pesquisa binária. Complete a função levelOrder fornecida em
seu editor para que ela imprima a passagem de ordem de nível da árvore de pesquisa binária.

Dica: você encontrará uma fila útil para completar este desafio.

Formato de entrada
O código stub bloqueado no seu editor lê as seguintes entradas e as monta em um BST:
A primeira linha contém um inteiro, T (o número de casos de teste).
As linhas subsequentes T contêm um inteiro, dados, denotando o valor de um elemento que deve ser
adicionado ao BST.

Formato de saída
Imprima o valor de dados de cada nó na travessia de ordem de nível da árvore como uma única linha de
N inteiros separados por espaços.

Entrada de amostra
6
3
5
4
7
2
1

Saída de Amostra
3 2 5 1 4 7

Explicação
A entrada forma a seguinte árvore de pesquisa binária:

Imagem no arquivo BST.png

Atravessamos cada nível da árvore da raiz para baixo e processamos os nós em cada nível da esquerda para
 a direita. A travessia da ordem de nível resultante é 3 -> 2 -> 5 -> 1 -> 4 -> 7, e nós imprimimos esses
 valores de dados como uma única linha de inteiros separados por espaços.
"""

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    from collections import deque
    def levelOrder(self,root):
        #Write your code here
        queue = self.deque([root]) if root else self.deque()

        while queue:
            node = queue.popleft()
            print(node.data, end=' ')

            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
