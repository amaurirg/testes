# pegando exceção criada manualmente

class ValorRepetido(Exception):
    def __init__(self, n):
        self.num = n

    def __str__(self):
        return f"Número {self.num} já foi digitado anteriormente."


def main():
    lista = []
    for i in range(3):
        while True:
            try:
                num= int(input("Escolha um número: "))
                break
            except ValueError:
                print("Somente números!")

        if num not in lista:
            lista.append(num)
        else:
            raise ValorRepetido(num)


if __name__ == "__main__":
    main()
