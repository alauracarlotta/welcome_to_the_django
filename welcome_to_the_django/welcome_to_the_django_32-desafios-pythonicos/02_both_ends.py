"""
02. both_ends

Dada uma string s, retorne uma string feita com os dois primeiros
e os dois ultimos caracteres da string original.
Exemplo: 'spring' retorna 'spng'. Entretanto, se o tamanho da string
for menor que 2, retorne uma string vazia.
"""

# Solution 1 - My preference: 
# (Limpo e pouco código)
""" 
def both_ends(s):
    # +++ SUA SOLUÇÃO +++
    if len(s) <= 2:
        return ''
    string = s
    initial_string = string[:2]
    end_string = string[-2:]
    return initial_string + end_string 
"""

# Solution 2:
""" 
def both_ends(s):
    # +++ SUA SOLUÇÃO +++
    return '' if len(s) <= 2 else s[:2] + s[-2:] 
"""

# Solution 3:
def both_ends(s):
    # +++ SUA SOLUÇÃO +++
    if len(s) <= 2:
        return ''
    
    initial_end = []
    cont = 0
    while len(initial_end) != 4:
        if len(initial_end) >= 2:
            initial_end.append(s[-(cont)])
            cont -= 1
        else:
            initial_end.append(s[cont])
            cont += 1
    return ''.join(initial_end)


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
    test(both_ends, 'spring', 'spng')
    test(both_ends, 'Hello', 'Helo')
    test(both_ends, 'a', '')
    test(both_ends, 'xyz', 'xyyz')
