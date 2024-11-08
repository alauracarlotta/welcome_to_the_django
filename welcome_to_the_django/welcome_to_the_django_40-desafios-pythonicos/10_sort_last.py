"""
10. sort_last

Dada uma lista de tuplas não vazias, retorne uma lista ordenada em ordem
crescente com base no último elemento de cada tupla.

Exemplo: [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
Irá retornar: [(2, 2), (1, 3), (3, 4, 5), (1, 7)]

Dica: Use uma custom key= function para extrair o ultimo elemento de cada tupla.
"""
def sort_last(tuples):
    from operator import itemgetter
    
    new_tuple_sorted = sorted(tuples, key=itemgetter(-1))

    return new_tuple_sorted


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(function, input, expected):
    """
    Executa a função f com o parâmetro input e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    output = function(input)

    if output == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {function.__name__}({input!r}) retornou {output!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(sort_last, [(1, 3), (3, 2), (2, 1)],
        [(2, 1), (3, 2), (1, 3)])
    test(sort_last, [(2, 3), (1, 2), (3, 1)],
        [(3, 1), (1, 2), (2, 3)])
    test(sort_last, [(1, 7), (1, 3), (3, 4, 5), (2, 2)],
        [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
    test(sort_last, [(1, 4, 6), (1, 2, 2), (2, 1, 3), (7, 5, 1)],
        [(7, 5, 1), (1, 2, 2), (2, 1, 3), (1, 4, 6)])
