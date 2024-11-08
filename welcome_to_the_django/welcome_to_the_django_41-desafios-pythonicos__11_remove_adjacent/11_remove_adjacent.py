"""
11. remove_adjacent

Dada uma lista de números, retorne uma lista onde todos elementos
adjacentes iguais são reduzidos a um único elemento.

Exemplo: [1, 2, 2, 3]
Irá retornar: [1, 2, 3]
"""

# WIP
# TODO:
    # Corrigir exercicio

def remove_adjacent(nums):
    # +++ SUA SOLUÇÃO +++
    if len(nums) <= 1:
        return nums

    lista = []
    for cont in range(len(nums) - 1):
        if cont == 0:
            if nums[cont] == nums[cont + 1]:
                lista.append(nums[cont + 1])
            else:
                lista.extend(nums[:2])
        else:
            if not nums[cont] == nums[cont + 1]:
                lista.append(nums[cont + 1])

    return lista


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(function, input, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
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
    test(remove_adjacent, [1, 2, 2, 3], [1, 2, 3])
    test(remove_adjacent, [2, 2, 3, 3, 3], [2, 3])
    test(remove_adjacent, [], [])
    test(remove_adjacent, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])
    test(remove_adjacent, [6], [6])
    test(remove_adjacent, [6, 6, 1, 2, 3, 3, 4, 5, 6, 6, 7], [6, 1, 2, 3, 4, 5, 6, 7])
    test(remove_adjacent, [0, 1, 2, 3, 3], [0, 1, 2, 3])
