"""
08. match_ends

Dada uma lista de strings, retorne a contagem do número de
strings onde o comprimento da cadeia é 2 ou mais e o primeiro
e o último caracteres da cadeia são os mesmos.

PS: Python não possui o operador ++, porém += funciona.
"""

def match_ends(words):
    # +++ SUA SOLUÇÃO +++
    plus_2_char = 0
    for word in words:
        word = word.upper()
        if len(word) >= 2:
            if word[0] == word[-1]:
                plus_2_char += 1
    return plus_2_char


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
    test(match_ends, ['aba', 'xyz', 'aa', 'x', 'bbb'], 3)
    test(match_ends, ['', 'x', 'xy', 'xyx', 'xx'], 2)
    test(match_ends, ['aaa', 'be', 'abc', 'hello'], 1)
    test(match_ends, ['Laura', 'Ana', 'Maria', 'hellie'], 1)