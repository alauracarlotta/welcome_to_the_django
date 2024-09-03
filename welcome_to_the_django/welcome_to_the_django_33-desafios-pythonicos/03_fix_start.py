"""
03. fix_start

Dada uma string s, retorne uma string onde
todas as ocorrências do primeiro caracter de s
foram substituidas por '*', exceto a primeira.

Exemplo: 'babble' retorna 'ba**le'

Assuma que a string tem tamanho 1 ou maior.

Dica: s.replace(stra, strb) retorna uma versão da string s
onde todas as instancias de stra foram substituidas por strb.
"""

# Solution 1 - My preference:
# Mais legível
""" def fix_start(string):
    if len(string) > 1:
        first_letter = string[0]
        new_string = ''
        for cont, value in enumerate(string):
            if cont == 0:
                new_string += value
            else:
                if value == first_letter:
                    value = value.replace(value, '*')
                new_string += value
    return new_string  """

# Solution 2
""" 
def fix_start(string):
    if len(string) > 1:
        first_letter = string[0]
        new_string = ''
        for cont in range(len(string)):
            if string.find(first_letter, cont) and not cont == 0:
                new_string += string[cont].replace(first_letter, '*')
            else:
                new_string += string[cont]
    return new_string
"""

# ('impar', 'par')[x%2==0]
"""numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros if x % 2 == 0]
print(pares)"""
# a = lambda x : x*5

# Solution 2
def fix_start(s):
    # return [a if a else 2 for a in [0,1,0,3]]
    return s[0] + ''.join([x if x != s[0] else x.replace(x, '*') for x in s[1:]])


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
    test(fix_start, 'babble', 'ba**le')
    test(fix_start, 'aardvark', 'a*rdv*rk')
    test(fix_start, 'google', 'goo*le')
    test(fix_start, 'donut', 'donut')
