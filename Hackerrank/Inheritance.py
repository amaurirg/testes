"""
Objetivo
Hoje, estamos investigando a herança.

Tarefa
Você recebe duas classes, Person e Student, em que Person é a classe base e Student é
a classe derivada. Código preenchido para Pessoa e uma declaração para Estudante são
fornecidas para você no editor. Observe que o aluno herda todas as propriedades da pessoa.

Complete a turma do aluno escrevendo o seguinte:
Um construtor da classe Student, que possui 4 parâmetros:
Uma string, firstName.
Uma string, lastName.
Um inteiro, id.
Uma matriz de inteiros (ou vetor) de pontuações de testes, pontuações.

Um método char calculate () que calcula a média de um objeto Student e retorna o caractere
de grau representativo de sua média calculada:

Escala de Classificação
Letra   Média
O       90 <= a <= 100
E       80 <= a <= 90
A       70 <= a <= 80
P       55 <= a <= 70
D       40 <= a <= 55
T       a < 40

Formato de entrada
O código stub bloqueado no seu editor chama seu construtor de classe Student e passa os
argumentos necessários. Também chama o método de cálculo (que não recebe argumentos).
Você não é responsável por ler a seguinte entrada de stdin:
A primeira linha contém firstName, lastName e id, respectivamente. A segunda linha contém o número de resultados do
teste. A terceira linha de números inteiros separados por espaços descreve scores.

Restrições
- 1 <= |firstName|,|lastName| <= 10
- |id| equivalente a 7
- 0 <= score, average <= 100

Formato de saída

Isso é tratado pelo código stub bloqueado no seu editor. Sua saída estará correta se o
seu construtor da classe Student e o método calculate () forem implementados corretamente.

Entrada de amostra
Heraldo Memelli 8135627
2
100 80

Saída de Amostra
Nome: Memelli, Heraldo
ID: 8135627
Grau: O

Explicação
Este aluno teve duas pontuações na média: 100 e 80. A nota média do aluno é (100 + 80) / 2 = 90.
Uma nota média de 90 corresponde à nota O, então nosso método calculate () deve retornar o caractere ' O '.

"""


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    """
    Construtor de Classe

    Parâmetros:
    firstName - Uma string que indica o primeiro nome da pessoa.
    lastName - Uma string que indica o sobrenome da pessoa.
    id - Um inteiro denotando o número de identificação da pessoa.
    scores - Uma matriz de números inteiros que indicam as pontuações dos testes da pessoa.

    Escreva seu construtor aqui
    """

    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    """
    Nome da função: calcular
    Retorno: um caractere que indica a nota.

    Escreva sua função aqui
    """
    def calculate(self):
        avg = sum(self.scores) / len(self.scores)
        if avg >= 90:
            return 'O'
        elif avg >= 80:
            return 'E'
        elif avg >= 70:
            return 'A'
        elif avg >= 55:
            return 'P'
        elif avg >= 40:
            return 'D'
        else:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
print(firstName, lastName, idNum)
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())