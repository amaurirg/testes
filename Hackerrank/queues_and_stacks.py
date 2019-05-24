"""
Bem-vindo ao dia 18! Hoje estamos aprendendo sobre pilhas e filas.

Um palíndromo é uma palavra, frase, número ou outra sequência de caracteres que lê o mesmo
para trás e para frente. Você pode determinar se uma determinada string, s, é um palíndromo?

Para resolver esse desafio, devemos primeiro pegar cada caractere em s, enfileirá-lo em uma fila e também
Empurre esse mesmo personagem para uma pilha. Feito isso, devemos remover o primeiro caractere
a fila e pop o caractere superior da pilha, em seguida, compare os dois caracteres para ver se eles
são os mesmos; contanto que os caracteres coincidam, continuamos dequeueing, popping e comparando cada
caractere até que nossos contêineres estejam vazios (um não-correspondência significa que não é um palíndromo).

Escreva as seguintes declarações e implementações:
Duas variáveis ​​de instância: uma para sua pilha e outra para sua fila.
Um método pushCharacter (charch) vazio que empurra um caractere para uma pilha.
Um método void enfileCharacter (charch) que enfileira um caractere na variável de instância da fila.
Um método char popCharacter () que aparece e retorna o caractere no topo da variável de instância da pilha.
Um método char dequeueCharacter () que desenfiltra e retorna o primeiro caractere na variável de instância da fila.

Formato de entrada
Você não precisa ler nada do stdin. O código stub bloqueado no seu editor lê uma única linha contendo string s.
Em seguida, chama os métodos especificados acima para passar cada caractere às suas variáveis ​​de instância.

Restrições
s é composto de letras inglesas minúsculas.

Formato de saída
Você não é responsável por imprimir qualquer saída para stdout.
Se o seu código estiver escrito corretamente e se for um palíndromo, o código stub bloqueado será impresso.
A palavra, s, é um palíndromo; caso contrário, ele irá imprimir A palavra, s, não é um palíndromo

Entrada de amostra
carro de corrida
Saída de Amostra

A palavra arara é um palíndromo.
"""

import sys


class Solution:
    # Write your code here
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, character):
        """ Um método pushCharacter (charch) vazio que empurra um caractere para uma pilha."""
        self.stack.append(character)

    def enqueueCharacter(self, character):
        """ Um método void enqueueCharacter (charch) que enfileira um caractere na variável de instância da fila. """
        self.queue.append(character)

    def popCharacter(self):
        """ Um método char popCharacter () que retira e retorna o caractere no topo da variável de instância da pilha. """
        return self.stack.pop()


    def dequeueCharacter(self):
        """ Um método char dequeueCharacter () que desenfileira e retorna o primeiro caractere na variável de instância da fila. """
        return self.queue.pop(0)


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop o caractere top da pilha
Dequeue o primeiro caractere da fila
comparar os dois caracteres
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")




# O código abaixo faz a mesma coisa
"""
s = input()
if s == s[::-1]:
    print(f"The word, {s}, is a palindrome.")
else:
    print(f"The word, {s}, is not a palindrome.")
"""
