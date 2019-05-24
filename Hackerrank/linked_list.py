"""
Objetivo
Hoje estamos trabalhando com listas vinculadas.

Uma classe Node é fornecida para você no editor. Um objeto Node possui um campo de dados inteiro,
dados e um ponteiro de instância Node, em seguida, apontando para outro nó (por exemplo, o próximo
nó em uma lista).

Uma função de inserção de nó também é declarada no seu editor. Ele possui dois parâmetros: um ponteiro,
um cabeçalho, apontando para o primeiro nó de uma lista vinculada e um valor de dados inteiro que deve
ser adicionado ao final da lista como um novo objeto Nó.

Tarefa
Complete a função de inserção em seu editor para que ela crie um novo Node (passe os dados como o argumento
do construtor Node) e insira-os na parte final da lista vinculada referenciada pelo parâmetro head. Depois
que o novo nó for adicionado, retorne a referência ao nó principal.

Nota: Se o argumento principal passado para a função de inserção for nulo, a lista inicial estará vazia.

Formato de entrada
A função insert possui 2 parâmetros: um ponteiro para um Node chamado head e um valor inteiro, data.
O construtor de Node possui 1 parâmetro: um valor inteiro para o campo de dados.
Você não precisa ler nada do stdin.

Formato de saída
Sua função de inserção deve retornar uma referência ao nó principal da lista vinculada.

Entrada de amostra
A entrada a seguir é manipulada para você pelo código bloqueado no editor:
A primeira linha contém T, o número de casos de teste.
Cada linha subseqüente de casos de teste contém um inteiro a ser inserido na cauda da lista.

4
2
3
4
1

Saída de Amostra
O código bloqueado em seu editor imprime os valores de dados ordenados para cada elemento em sua lista como
uma única linha de inteiros separados por espaços:

2 3 4 1

Explicação
T = 4, então o código bloqueado no editor estará inserindo 4 nós.
A lista está inicialmente vazia, então head é null; respondendo por isso, nosso código retorna um novo nó
contendo o valor de dados 2 como o líder de nossa lista. Em seguida, criamos e inserimos os nós 3, 4 e 1 no
final da nossa lista. A lista resultante retornada pela última chamada a ser inserida é [2, 3, 4, 1], portanto
a saída impressa é 2 3 4 1.

Existe um arquivo linked_list.png que contém uma explicação a mais.
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
    #Complete this method
        if (head == None):
            head = Node(data)
        else:
            head.next = self.insert(head.next, data)
        return head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head)
