# NOT BAD

TODO:

* ✅ Usar .find()
    => Utilizado no principal exercício (mais recente)

* ✅ Usar .replace()
    => Utilizado em todos os exercícios

* TODO: Próprio algoritmo __(? Não entendi, perguntar para o Wellington ?)__

* TODO: Expressoes regulares

* TODO: Incrementar o enuciado - "novo requisito para o projeto":
  * Ex:
    => Se aparecer 'not, not bad', pegamos o 1º ou 2º not?
    => E se houver not bad 2x, vai mudar as duas aparições?
    => Se aparecer o bad 1º e depois um not bad, o que acontecerá?

* TODO: É possível deixar o codigo organizado, expressivo e bem sucinto: __Use expressões regulares__!
    => Voltaremos aqui após a aula 45

## Exercícios que eu executei na primeira vez

__SOLUTION 1__
`def not_bad(s):`
    # +++ SUA SOLUÇÃO +++
    string_received = s
    index_not = string_received.find('not')
    index_bad = string_received.find('bad')
    not_before_bad = False
    result = ''

    if index_not > index_bad:
        return s
    if index_not < index_bad:
        not_before_bad = True
    if not_before_bad:
        index_slice = slice(string_received.index('not'))
        result = string_received[index_slice] + 'good!'
    # breakpoint()

    return result
