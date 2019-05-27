"""
Tarefa
Uma classe Node é fornecida para você no editor. Um objeto Node possui um campo de dados inteiro,
dados e um ponteiro de instância Node, em seguida, apontando para outro nó (por exemplo, o próximo
nó em uma lista).

Uma função removeDuplicates é declarada em seu editor, que leva um ponteiro para o nó principal de
uma lista vinculada como um parâmetro. Conclua o removeDuplicates para que exclua todos os nós
duplicados da lista e retorne o cabeçalho da lista atualizada.

Nota: O ponteiro da cabeça pode ser nulo, indicando que a lista está vazia. Certifique-se de redefinir
seu próximo ponteiro ao executar exclusões para evitar a quebra da lista.

Formato de entrada
Você não precisa ler nenhuma entrada de stdin. A entrada a seguir é manipulada pelo código stub bloqueado
e passada para a função removeDuplicates:
A primeira linha contém um inteiro, N, o número de nós a serem inseridos.
As N linhas subsequentes contêm um inteiro descrevendo o valor de dados de um nó sendo inserido na cauda
da lista.

Restrições

Os elementos de dados do argumento da lista encadeada sempre estarão em ordem não decrescente.
Formato de saída

Sua função removeDuplicates deve retornar o cabeçalho da lista vinculada atualizada. O código stub bloqueado
no seu editor irá imprimir a lista retornada para stdout.

Entrada de amostra
6
1
2
2
3
3
4

Saída de Amostra
1 2 3 4

Explicação
N = 6, e nossa lista não decrescente é [1, 2, 2, 3, 3, 4]. Os valores 2 e 3 ocorrem duas vezes na lista,
portanto, removemos os dois nós duplicados. Em seguida, retornamos nossa lista atualizada (crescente),
que é [1, 2, 3, 4].
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        node = head

        while node:
            if node.next:
                if node.data == node.next.data:
                    node.next = node.next.next
                    continue

            node = node.next

        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head)