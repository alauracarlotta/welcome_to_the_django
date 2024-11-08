# MATH ENDS

TODO:

* ✅ Adição em place (incrementa um contador) / Forma simples: Respeitando a condição e incrmentando um contador.
    => Usei um incrmentador para fazer a contagem.

* TODO: Use 'list comprehention', criando uma lista que respeita a mesma restrição

* TODO: Generator expresions = Acumula-se o 1 e utiliza-se o sum para chegar no valor final da contagem

## Lembre-se

__Nem sempre o código mais sofisticado é o melhor!__

__Quase sempre, a solução mais óbvia e mais simples costuma ser a mais eficiente em termos de memória, legibilidade e manutenabilidade!__

__Nem sempre usar recursos avançados significa que você conseguirá executar o melhor código.__

## Exercícios que eu executei na primeira vez

__SOLUTION 1__
`def match_ends(words):`
    # +++ SUA SOLUÇÃO +++

    count_words = 0

    for cont in range(len(words)):
        if len(words[cont]) < 2:
            result = 0
        else:
            if words[cont][0] == words[cont][-1]:
                count_words += 1
            result = count_words

    return result
