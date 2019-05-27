"""
Objetivo
Hoje, estamos trabalhando com árvores de pesquisa binária (BSTs).

Tarefa
A altura de uma árvore de pesquisa binária é o número de arestas entre a raiz da árvore e sua
folha mais distante. Você recebe um ponteiro, root, apontando para a raiz de uma árvore de pesquisa
binária. Complete a função getHeight fornecida em seu editor para que ela retorne a altura da árvore
de pesquisa binária.

Formato de entrada
O código stub bloqueado no seu editor lê as seguintes entradas e as monta em uma árvore de pesquisa binária:
A primeira linha contém um inteiro, n, denotando o número de nós na árvore.
Cada uma das n linhas subsequentes contém um inteiro, dados, denotando o valor de um elemento que deve
ser adicionado ao BST.

Formato de saída
O código stub bloqueado no seu editor irá imprimir o número inteiro retornado pela sua função getHeight
denotando a altura do BST.

Entrada de amostra

7
3
5
2
1
4
6
7
Saída de Amostra

3

OBS: Existe um arquivo binary_search_trees.png com mais explicações
A entrada forma o seguinte BST:

BST.png -> primeira imagem do arquivo

O caminho mais longo da raiz para a folha é mostrado abaixo:

Maior RTL.png -> segunda imagem do arquivo

Existem 4 nós neste caminho que estão ligados por 3 arestas, o que significa a altura
do nosso BST = 3. Assim, imprimimos 3 como a nossa resposta.
"""

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

    def getHeight(self, root):
        #Write your code here
        if root:
            leftDepth = self.getHeight(root.left)
            rightDepth = self.getHeight(root.right)
            return max(leftDepth, rightDepth) + 1
        else:
            return -1

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)