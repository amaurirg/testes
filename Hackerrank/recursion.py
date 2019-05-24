"""
Objetivo
Atualmente, estamos aprendendo e praticando um conceito algorítmico chamado Recursão .

Método Recursivo para Cálculo Fatorial

factorial(N) = { 1                      N <= 1
                 N x Factorial(N - 1)   otherwise }

Tarefa
Grave uma função fatorial que recebe um inteiro positivo N como um parâmetro e imprime o resultado de
( fatorial). N!N
Nota: Se você não usar a recursão ou não nomear sua função recursiva fatorial ou Factorial ,
você receberá uma pontuação de 0.

Formato de entrada
Um único inteiro, N (o argumento para passar para fatorial ).

Restrições
- 2 <= N <= 12
- Seu envio deve conter uma função recursiva denominada fatorial .

Formato de saída
Imprima um único inteiro denotando. N!

Entrada de amostra
3

Saída de Amostra
6

Explicação
Considere os seguintes passos:
1 - factorial(3) = 3 x factorial(2)
2 - factorial(2) = 2 x factorial(1)
3 - factorial(1) = 1


Dos passos 2 e 3, podemos dizer factorial(2) = 2 x 1 = 2; então, quando aplicamos o valor de factorial(2) para
o passo 1 , obtemos factorial(3) = 3 x 2 x 1 = 6.
Assim, imprimimos 6 como nossa resposta.

"""

i = 1
fat = 1
n = int(input("Digite o número: "))

while i <= n:
    fat *= i
    i += 1

print(f'Fat({n}) = {fat}')
