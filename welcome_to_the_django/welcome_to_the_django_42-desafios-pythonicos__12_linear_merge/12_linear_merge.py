"""
12. linear_merge

Dada duas listas ordenadas em ordem crescente, crie e retorne uma lista
com a combinação das duas listas, também em ordem crescente. Você pode
modificar as listas recebidas.

A sua solução deve rodar em tempo linear, ou seja, deve fazer uma
única passagem em cada uma das listas.
"""

""" def linear_merge(list1, list2):
    new_list = list1 + list2
    # +++ SUA SOLUÇÃO +++
    return sorted(new_list) """

""" def intercala(L,L2):
    intercalada = []
    for a,b in zip(L, L2):
        intercalada.append(a)
        intercalada.append(b)
    return intercalada

lista1 = [1,2,3]
lista2 = [4,5,6]

listaIntercalada = intercala(lista1, lista2)

for i in listaIntercalada:
    print i """


""" def linear_merge(list1, list2):
    import heapq
    new_value = heapq.merge(list1, list2)
    print(new_value)
    return list(new_value) """

""" def linear_merge(*lista):
    import heapq
    return list(heapq.merge(*lista)) """

# WIP
# TODO:
    # Corrigir exercicio

def linear_merge(lista1, lista2):
    import heapq

    heaps_combinados = heapq.merge(lista1, lista2)
    lista_combinada = list(heaps_combinados)

    return lista_combinada

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(function, input, expected):
    """
    Executa a função function com o parâmetro input e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função function está correta ou não.
    """
    output = function(*input)

    if output == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {function.__name__}{input!r} retornou {output!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(linear_merge, (['aa', 'xx', 'zz'], ['bb', 'cc']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'xx'], ['bb', 'cc', 'zz']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'aa'], ['aa', 'bb', 'bb']),
        ['aa', 'aa', 'aa', 'bb', 'bb'])
    test(linear_merge, (['aa', 'aa'], ['aa', 'bb', 'bb']),
        ['aa', 'aa', 'aa', 'bb', 'bb']) 
    test(linear_merge, ([4, 8, 10, 1], [6, 2, 3, 9]),  
        [4, 6, 2, 3, 8, 9, 10, 1])
    test(linear_merge, (['aa', 'xx', 'bb'], ['cc', 'dd', 'ff']),
        ['aa', 'cc', 'dd', 'ff', 'xx', 'bb'])
    test(linear_merge, ([93, 96, 53], [67, 90, 82]),
        [67, 90, 82, 93, 96, 53])
    test(linear_merge, ([69, 1, 46], [71, 31, 57]),
        [69, 1, 46, 71, 31, 57])
    test(linear_merge, ([4, 43, 36], [62, 68, 27]),
        [4, 43, 36, 62, 68, 27])
    test(linear_merge, ([97, 85, 78], [74, 50, 18]),
        [74, 50, 18, 97, 85, 78])
    test(linear_merge, ([5, 7, 1], [4, 8, 9]),
        [4, 5, 7, 1, 8, 9])
    test(linear_merge, ([19, 92, 95], [3, 61, 29]),
        [3, 19, 61, 29, 92, 95])
    test(linear_merge, ([45, 73, 34], [1, 74, 5]),
        [1, 45, 73, 34, 74, 5])
    test(linear_merge, ([15, 37, 97], [76, 60, 41]),
        [15, 37, 76, 60, 41, 97])
    test(linear_merge, ([56, 77, 18], [33, 58, 47]),
        [33, 56, 58, 47, 77, 18])
    test(linear_merge, ([7, 31, 80], [16, 10, 44]),
        [7, 16, 10, 31, 44, 80])
    test(linear_merge, ([48, 78, 79], [52, 6, 98]),
        [48, 52, 6, 78, 79, 98])
    test(linear_merge, ([38, 14, 63], [39, 89, 90]),
        [38, 14, 39, 63, 89, 90])
    test(linear_merge, ([27, 13, 84], [42, 30, 20]),
        [27, 13, 42, 30, 20, 84])
    test(linear_merge, ([59, 19, 35], [97, 11, 60]),
        [59, 19, 35, 97, 11, 60])
    test(linear_merge, ([43, 28, 62], [2, 63, 74]),
        [2, 43, 28, 62, 63, 74])
