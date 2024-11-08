# SORT LAST

TODO:

* ✅ O sorted permite passar uma key = passar uma função que vai influenciar na lógica do algoritmo de ordenação
* Fazer um sort na mão (Impelmentado com uma função)
* função anonima com a expressãp lambda
* definir uma função que fará o papel de chave e passar para o key também
procurar no python a biblioteca padrão getitem (que faz parte do repertório de programação funcional da linguagem)

## Exercícios que eu executei na primeira vez

__SOLUTION 1__
`def sort_last(tuples):`
    from operator import itemgetter

    new_tuple_sorted = sorted(tuples, key=itemgetter(-1))

    return new_tuple_sorted
