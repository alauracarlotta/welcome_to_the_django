"""
05. verbing

Dada uma string, se seu tamanho for pelo menos 3,
adicione 'ing' no seu fim, a menos que a string
já termine com 'ing', nesse caso adicione 'ly'.

Se o tamanho da string for menor que 3, não altere nada.

Retorne o resultado da string.
"""

# SOLUTION 1 - MY PREFERENCE:
# Código limpo e curto
def verbing(verb):
    # +++ SUA SOLUÇÃO +++
    if len(verb) > 3:
        if 'ing' in verb[-3:]:
            verb = ''.join([verb, 'ly'])
        
        else:
            verb = ''.join([verb, 'ing'])
    
    return verb


# SOLUTION 2
""" 
def verbing(s):
    return (''.join([s, 'ly']) if 'ing' in s[-3:] else ''.join([s, 'ing'])) if len(s) > 3 else s
"""


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---
def test(function, input, expected):
    """
    Executa a função function com o parâmetro input e compara o resultado com expected.
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
    test(verbing, 'hail', 'hailing')
    test(verbing, 'swiming', 'swimingly')
    test(verbing, 'swimingo', 'swimingoing')
    test(verbing, 'do', 'do')
    test(verbing, 'dos', 'dos')
