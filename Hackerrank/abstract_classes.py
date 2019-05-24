"""
Objetivo
Hoje, estamos pegando o que aprendemos ontem sobre Herança e estendendo-o para o Abstract Classes.
Como esse é um conceito orientado a objetos muito específico, as submissões estão limitadas aos poucos
idiomas que usam essa construção.

Tarefa
Dada uma classe Book e uma classe Solution, escreva uma classe MyBook que faça o seguinte:

Herda de livro
Tem um construtor parametrizado, tomando estes 3 parâmetros:
string title
string author
int price

Implementa o método abstract display () da classe Book para que imprima estas 3 linhas:
Título, um espaço e, em seguida, a instância atual.
Autor, um espaço e, em seguida, a instância atual.
Preço, um espaço e, em seguida, o da instância atual.

Nota: Como essas classes estão sendo gravadas no mesmo arquivo, você não deve usar um modificador de
acesso (por exemplo, public) ao declarar MyBook ou seu código não será executado.

Formato de entrada
Você não é responsável por ler qualquer entrada de stdin. A classe Solution cria um objeto Book e chama
o construtor de classe MyBook (passando os argumentos necessários). Em seguida, chama o método de
exibição no objeto Book.

Formato de saída
O método void display () deve imprimir e rotular o respectivo título, autor e preço da instância do
objeto MyBook (com cada valor em sua própria linha) da seguinte forma:

Título: $ title
Autor: $ author
Preço: $ preço
Nota: O $ é prefixado aos nomes das variáveis ​​para indicar que eles são espaços reservados para variáveis.

Entrada de amostra
A seguinte entrada do stdin é manipulada pelo código stub bloqueado no seu editor:

O Alquimista
Paulo Coelho
248

Saída de Amostra
A seguinte saída é impressa pelo seu método display ():
Título: O Alquimista
Autor: Paulo Coelho
Preço: 248
"""

from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    @abstractmethod
    def display(self):
        pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price

    def display(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nPrice: {self.price}")


title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
