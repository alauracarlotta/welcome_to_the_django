"""
06. not_bad

Dada uma string, encontre a primeira aparição das
substrings 'not' e 'bad'. Se 'bad' aparecer depois
de 'not', troque todo o trecho entre 'not' e 'bad'
por 'good' e retorne a string resultante.

Exemplo: 'The dinner is not that bad!' retorna 'The dinner is good!'
"""

def not_bad(string):
    # +++ SUA SOLUÇÃO +++
    subs_not = string.find('not')
    subs_bad = string.find('bad')
    if subs_not < subs_bad:
        string = string.replace(string[subs_not:(subs_bad + 3)], 'good')
    
    return string


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
    test(not_bad, 
        'This movie is not so bad!',
        'This movie is good!'
    )

    test(not_bad,
        'This movie is not so bad, baby!', 
        'This movie is good, baby!'
    )
    
    test(not_bad,
        'This dinner is not that bad!',
        'This dinner is good!'
    )
    
    test(not_bad,
        'This tea is not hot',
        'This tea is not hot'
    )
    
    test(not_bad,
        "It's bad yet not",
        "It's bad yet not"
    )
