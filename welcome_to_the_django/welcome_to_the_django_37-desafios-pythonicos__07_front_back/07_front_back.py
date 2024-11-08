"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""

def front_back(a, b):
    # +++ SUA SOLUÇÃO +++
    list_words = [a, b]
    front = []
    back = []
    for word in list_words:
        size = int(len(word) / 2)
        if len(word) % 2 == 0:
            front.append(word[:size])
            back.append(word[size:])
        else:
            front.append(word[:size + 1])
            back.append(word[size + 1:])
    front_words = ''.join(front)
    back_words = ''.join(back)
    
    return ''.join([front_words, back_words])

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---
def test(function, input, expected):
    """
    Executa a função f com o parâmetro input e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
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
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
    test(front_back, ('Laura', 'Wellington'), 'LauWellirangton')
