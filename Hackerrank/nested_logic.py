"""
Objetivo
O desafio de hoje coloca sua compreensão de instruções condicionais aninhadas para o teste.

Tarefa
Sua biblioteca local precisa da sua ajuda! Dadas as datas de retorno esperadas e reais para um
livro da biblioteca, crie um programa que calcule a multa (se houver). A estrutura de taxas é a seguinte:

1 - Se o livro for devolvido antes da data de retorno esperada, não será cobrada qualquer multa
(por exemplo, multa = 0).
2 - Se o livro for devolvido após o dia de retorno esperado, mas ainda dentro do mesmo mês e ano de
calendário que a data de retorno esperada, multa = 15 Hackos x (o número de dias de atraso).
3 - Se o livro for devolvido após o mês de retorno esperado, mas ainda dentro do mesmo ano de calendário
da data de retorno esperada, a multa = 500 Hackos x (o número de meses de atraso).
4 - Se o livro for devolvido após o ano civil em que era esperado, há uma multa fixa de 10000 Hackos.

Formato de entrada
A primeira linha contém 3 inteiros separados por espaços denotando o respectivo dia, mês e ano em que o
livro foi realmente retornado.
A segunda linha contém 3 inteiros separados por espaços denotando o respectivo dia, mês e ano em que se
esperava que o livro fosse retornado (data de vencimento).

Restrições
1 <= D <= 31
1 <= M <= 12
1 <= Y <= 3000
É garantido que as datas serão válidas nas datas do calendário gregoriano.

Formato de saída
Imprima um único inteiro indicando a multa da biblioteca para o livro recebido como entrada.

Entrada de amostra
9 6 2015
6 6 2015

Saída de Amostra
45

Explicação
Dadas as seguintes datas de retorno:
Real:       Da = 9, Ma = 6, Ya = 2015
Esperado:   De = 6, Me = 6, Ye = 2015

Porque Ye = Ya, sabemos que está menos de um ano atrasado.
Porque Me = Ma, sabemos que está menos de um mês atrasado.
Porque De < Da, sabemos que foi devolvido tarde (mas ainda dentro do mesmo mês e ano).

Pela estrutura de taxas da biblioteca, sabemos que nossa multa será de 15 Hackos x (# dias de atraso).
Em seguida, imprimimos o resultado de 15 x (Da - De) = 15 x (9 - 6) = 45 como nossa saída.

A explicação original encontra-se em nested_logic.png
"""

#RESUMO
"""
até a data = 0
no mês e ano = 15 x dias atraso
outro mês mesmo ano = 500 x meses atraso
outro ano = 10000 
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

ret = input()
exp = input()

ad, am, ay = map(int, ret.strip().split())
ed, em, ey = map(int, exp.strip().split())

if ay > ey:
    print(10000)
elif ay == ey and am > em:
    print((am-em)*500)
elif ay == ey and am == em and ad > ed:
    print((ad-ed)*15)
else: print(0)
