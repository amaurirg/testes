"""
TAREFA:
Dados nomes e números de telefone, monte uma lista telefônica que mapeie os nomes dos amigos para
seus respectivos números de telefone. Em seguida, você receberá um número desconhecido de nomes para
consultar sua agenda telefônica. Para cada n consultado, imprima a entrada associada de sua lista
telefônica em uma nova linha no nome do formulário = phoneNumber; se uma entrada para n não for
encontrada, imprima Não encontrado.


INPUT:
A primeira linha contém um inteiro, n, indicando o número de entradas na lista telefônica.
Cada uma das n linhas subsequentes descreve uma entrada na forma de dois valores separados por espaço
em uma única linha. O primeiro valor é o nome de um amigo e o segundo valor é um número de telefone de
oito dígitos.

Após as n linhas de entradas do catálogo telefônico, há um número desconhecido de linhas de consultas.
Cada linha (consulta) contém um nome para procurar e você deve continuar lendo as linhas até que não
haja mais entrada.

Nota: Os nomes consistem em letras alfabéticas inglesas minúsculas e são apenas nomes próprios.


OUTPUT:
Em uma nova linha para cada consulta, imprima Não encontrado se o nome não tiver entrada correspondente
na lista telefônica; caso contrário, imprima o nome completo e phoneNumber no formato Nome = número de telefone.


SIMPLE OUTPUT:
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry


SAMPLE OUTPUT:
sam=99912222
Not found
harry=12299933


EXPLICAÇÃO:

Adicionamos os seguintes pares n=3(chave, valor) ao nosso mapa para que fique assim:
phoneBook = {(sam, 99912222), (tom, 11122222), (harry, 12299933)}
Em seguida, processamos cada consulta e imprimimos key = value se o questionado for encontrado no mapa;
Caso contrário, imprimimos não encontrado.

Consulta 0: sam
Sam é uma das chaves do nosso dicionário, por isso imprimimos sam = 99912222.

Consulta 1: edward
Edward não é uma das chaves do dicionário, então imprimimos não encontrado.

Consulta 2: harry
Harry é uma das chaves em nosso dicionário, então nós imprimimos harry = 12299933.
"""

# n = int(input())
n= 100000
telephone_book = {}


# n = int(input())
# telephone_book = {}

f = open("input_HR.txt")

lista = []

for s in f.readlines():
    (',').join(s)
    lista.append(s.strip())

# print(lista)

for each in lista:
    name, phone = each.split(' ')
    telephone_book[name] = phone

print(telephone_book)

f = open("input_search.txt")

search = []

for s in f.readlines():
    search.append(s.strip())

print(search)

for i in search:
    if i in telephone_book:
        print(f"{i}={telephone_book[i]}")
    else:
        print('Not found')


"""
n = int(input())
telephone_book = {}

for each in range(n):
    name, phone = input().split(' ')
    telephone_book[name] = phone

for i in range(n):
    name = input()
    if name in telephone_book:
        print(f"{name}={telephone_book[name]}")
    else:
        print('Not found')

"""

"""
O QUE DEU CERTO FOI ESSE ABAIXO:

n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {k: v for k,v in name_numbers}
while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break
        
"""