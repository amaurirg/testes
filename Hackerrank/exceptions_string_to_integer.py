"""
Objetivo
Hoje, estamos começando com Exceções aprendendo a analisar um inteiro a partir de uma string e a
imprimir uma mensagem de erro personalizada.

Tarefa
Leia uma string, S, e imprima seu valor inteiro; se S não puder ser convertido em um inteiro, imprima
a Cadeia de caracteres inválida.

Nota: Você deve usar o String-to-Integer e as construções de manipulação de exceção incorporadas no
seu idioma de envio. Se você tentar usar loops / declarações condicionais, você receberá uma pontuação 0.

Formato de entrada
Uma única corda, S.

Restrições
1 <= | S | <= 6, onde | S | é o comprimento da string S.
S é composto de letras minúsculas (a-z) ou dígitos decimais (0-9).

Formato de saída
Imprima o valor inteiro analisado de S ou Bad String se S não puder ser convertido em um inteiro.

Entrada de Amostra 0
3

Amostra de Saída 0
3

Entrada de amostra 1
za

Exemplo de Saída 1
Bad String

Explicação
O Caso de Amostra 0 contém um número inteiro, portanto, ele não deve gerar uma exceção quando
tentarmos convertê-lo em um inteiro. Assim, imprimimos o 3.
O exemplo de caso 1 não contém números inteiros, portanto, uma tentativa de convertê-lo em um
inteiro gerará uma exceção. Assim, nosso manipulador de exceções imprime Bad String.
"""

import sys


S = input().strip()

try:
    print(int(S))
except ValueError:
    print("Bad String")