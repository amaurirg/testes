# pegando excessão com intervalo de números

try:
    a = int(input("Digite um número de 1 a 20: "))
    if not 1 <= a <= 20:
        raise ValueError
    else:
        print("Ok")
except ValueError:
    print("Número inválido!")
