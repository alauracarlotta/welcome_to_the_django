# FRONT X

TODO:

* ✅ Dividir e conquistar: Dividir a ordenação em duas listas.
    => Conforme o enunciado já dá a dica de executar o código em duas listas, fiz dessa forma, onde separa as palavras que começam com 'x' e as que NÃO começam com 'x'.

* ✅ Mantenha a semântica dos problemas, nomeando as variáveis com nomes expressivos e contudentes.
    => Nomeei ambas as listas respectivamente: 'init_letter_x' (as que começam com a letra x) e 'not_initialized_x' (as que NÃO começam com a letra 'x')

* TODO: Quants ordenações estão sendo feitas?
  * é possivel executar com a penas um .sorted()

* TODO: Executar utilizando o list comprehations

* TODO: Executar utilizando o generator expresions

* TODO: Hack+++ => subverter a função de ordenação que o próprio python já tem, passando uma função que vai mudar a lógica da ordenação

## Exercícios que eu executei na primeira vez

__SOLUTION 1__
`def front_x(list_value):`
    # +++ SUA SOLUÇÃO +++
    list_words = list_value
    list_start_x_letter = []
    list_other_words = []
    for word in list_words:
        if word[0] == 'x':
            list_start_x_letter.insert(0, word)

        else:
            list_other_words.insert(0, word)

    order_start_x = sorted(list_start_x_letter)
    order_other_words = sorted(list_other_words)
    complete_list = order_start_x + order_other_words
    # breakpoint()
    return complete_list
