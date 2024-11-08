# BOTH ENDS

TODO:

* ✅ usar o slice()
    => Neste caso, usei o fateamento com índice do python, o slice [::]

* ✅ fazer o código em uma única linha
    => Neste caso, usei o ternário que inclusive ficou bem curtinho.

* ✅ (Se muito fácil) usar while pra contar as letras na mão
    => ficou bem mais trabalhoso e menos legível. Contudo o ex foi conclído.

## Exercícios que eu executei na primeira vez

__SOLUÇÃO 1__
`def both_ends(s):`
    string_received = s
    if len(string_received) < 2:
        result = ''
    else:
        result = f'{string_received[0]}{string_received[1]}{string_received[-2]}{string_received[-1]}'
    return result

***

__SOLUÇÃO 2__
`def both_ends(s):`
    string_received = s
    if len(string_received) < 2:
        result = ''
    else:
        initial_string = slice(2)
        final_string = slice(-2, len(string_received))
        result = string_received[initial_string] + string_received[final_string]
    return result

***

__SOLUÇÃO 3__
`def both_ends(s):`
    return '' if len(s) < 2 else s[slice(2)] + s[slice(-2, len(s))]

***

__SOLUÇÃO 4__
`def both_ends(s):`
    result = []
    if len(s) > 2:
        # TODO 1 while só
        cont = 0
        while not len(result) == 4:
            result.insert(cont, s[cont])
            result.insert(cont + 1, s[-(cont + 1)])
            cont += 1
        new_string = ''.join(result)

    else:
        new_string = ''
    return new_string

***

__SOLUÇÃO 5__
`def both_ends(s):`
    # +++ SUA SOLUÇÃO +++

    # Refatoração de código
    if len(s) <= 2:
        return ''

    new_string = []
    cont = 0
    while not len(new_string) == 4:
        new_string.insert(cont, s[cont])
        new_string.insert(cont + 1, s[-(cont + 1)])
        cont += 1
    result = ''.join(new_string)
