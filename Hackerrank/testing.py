"""
Esse problema é todo sobre o teste de unidade.

Sua empresa precisa de uma função que atenda aos seguintes requisitos:

Para uma dada matriz de n inteiros, a função retorna o índice do elemento com o valor mínimo na matriz.
Se houver mais de um elemento com o valor mínimo, o índice retornado deverá ser o menor.
Se uma matriz vazia for passada para a função, ela deverá gerar uma exceção.
Nota: As matrizes são indexadas de 0.

Um colega escreveu essa função e sua tarefa é projetar 3 testes unitários separados, testando se a função
se comporta corretamente. A implementação em Python está listada abaixo (implementações em outros idiomas
podem ser encontradas no modelo de código):

def minimum_index(seq):
    if len(seq) == 0:
        # "Não é possível obter o índice de valor mínimo de uma sequência vazia"
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

Outro colega de trabalho preparou funções que executarão o teste e validarão os resultados retornados com
expectativas. Sua tarefa é implementar três classes que produzirão dados de teste e os resultados esperados
para as funções de teste. Mais especificamente: function get_array () na classe TestDataEmptyArray e funções
get_array () e get_expected_result () nas classes TestDataUniqueValues ​​e TestDataExactlyTwoDifferentMinimums
seguindo as especificações abaixo:

Método get_array () na classe TestDataEmptyArray tem que retornar uma matriz vazia.
O método get_array () na classe TestDataUniqueValues ​​deve retornar uma matriz de tamanho de pelo menos 2
com todos os elementos exclusivos, enquanto o método get_expected_result () dessa classe deve retornar o
índice de valor mínimo esperado para essa matriz.
O método get_array () da classe TestDataExactlyTwoDifferentMinimums deve retornar uma matriz onde existem
exatamente dois valores mínimos diferentes, enquanto o método get_expected_result () dessa classe deve
retornar o índice de valor mínimo esperado para essa matriz.
Dê uma olhada no modelo de código para ver a implementação exata das funções que seus colegas já implementaram.
"""


def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx


class TestDataEmptyArray(object):

    @staticmethod
    def get_array():


# complete this function

class TestDataUniqueValues(object):

    @staticmethod
    def get_array():

    # complete this function

    @staticmethod
    def get_expected_result():


# complete this function

class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():

    # complete this function

    @staticmethod
    def get_expected_result():


# complete this function


def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")
