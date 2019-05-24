"""
Objetivo
O desafio de ontem ensinou você a gerenciar situações excepcionais usando blocos try e catch.
No desafio de hoje, você vai praticar lançar e propagar uma exceção.

Tarefa
Escreva uma classe Calculator com um único método: int power (int, int). O método power usa
dois inteiros, n e p como parâmetros e retorna o resultado inteiro de n**p. Se n ou p for
negativo, o método deve lançar uma exceção com a mensagem: n e p devem ser não-negativos.
Nota: Não use um modificador de acesso (por exemplo, público) na declaração da sua classe Calculator.

Formato de entrada
A entrada de stdin é manipulada para você pelo código stub bloqueado no editor. A primeira linha
contém um inteiro, T, o número de casos de teste. Cada uma das linhas T subsequentes descreve um
caso de teste em 2 inteiros separados por espaços denotando n e p, respectivamente.

Restrições
- Nenhum caso de teste resultará em estouro para código escrito corretamente.

Formato de saída
A saída para stdout é manipulada para você pelo código stub bloqueado em seu editor. Existem T linhas
de saída, onde cada linha contém o resultado de n**p como calculado pelo método de potência da sua
classe Calculator.

Entrada de amostra
4
3 5
2 4
-1 -2
-1 3

Saída de Amostra
243
16
n e p devem ser não negativos
n e p devem ser não negativos

Explicação
 T = 4
T0: 3 e 5 são positivos, então power retorna o resultado de 3**5, que é 243.
T1: 2 e 4 são positivos, então power retorna o resultado de 2**4 =, que é 16.
T2: Ambas as entradas (-1 e -2) são negativas, portanto, a potência lança uma exceção e n e p devem
ser não-negativos.
T3: Uma das entradas () é negativa, então o poder gera uma exceção e n e p não deve ser negativo é impresso.
"""

#Write your code here
class Calculator:
    def power(self, n, p):
        if n < 0 or p < 0:
            return "n and p should be non-negative"
        return n**p


myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)

