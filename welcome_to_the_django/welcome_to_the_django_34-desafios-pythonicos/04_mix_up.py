"""
04. mix_up

Dadas as strings a e b, retorne uma string com a e b separados
por um espaço '<a> <b>', além disso, troque os 2 primeiros caracteres
das duas strings.

Exemplo:
    'mix', 'pod' -> 'pox mid'
    'dog, 'dinner' -> 'dig donner'

Assuma que a e b tem tamanho 2 ou maior.
"""

# SOLUTION 1 - MY PREFERENCE:
# Mais limpo e inchuto
def mix_up(a, b):
    # +++ SUA SOLUÇÃO +++
    if (len(a) and len(b)) <= 2:
        return ' '. join([a, b])

    word_a = b[:2] + a[2:]
    word_b = a[:2] + b[2:]

    return ' '.join([word_a, word_b])


# SOLUTION 2
""" 
def mix_up(a, b):
    return f'{b[:2] + a[2:]} {a[:2] + b[2:]}' if len(a) > 2 or len(b) > 2 else f'{a} {b}' 
"""


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(function, input, expected):
    """
    Executa a função function com o parâmetro input e compara o resultado com expected.
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
    test(mix_up, ('mix', 'pod'), 'pox mid')
    test(mix_up, ('dog', 'dinner'), 'dig donner')
    test(mix_up, ('gnash', 'sport'), 'spash gnort')
    test(mix_up, ('pezzy', 'firm'), 'fizzy perm')
    test(mix_up, ('hb', 'bh'), 'hb bh')
    test(mix_up, ('a', 'bh'), 'a bh')
