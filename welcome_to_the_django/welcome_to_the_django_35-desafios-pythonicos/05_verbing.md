# VERBING

TODO:

* ✅ Oportunidade de verificar posições estéticas do código
    => Código ficou bem curto

* ✅ 3 caminhos lógicos (ou 4)
    => 1. Acresecentando 'ly'; 2. Acrescentando 'ing'; 3. Não acrescentando nada pois o tamanho não foi o suficiente.

* ✅ Como o exercício é sobre manipulação de verbos, tenha isso como inspiração para nomear as variáveis (nada de s, x, etc.)
    => Adicionada nomenclatura semântica.

* ✅ Executar o exercício numa unica linha
    => Exercício executado, porém a apresentação dele ficou bem feia rs
    => Consegui adicionar um ternário 'novo'

* ✅ Isolar o procesamento, o caminho de tomada de decisão para validar apenas o que o eununciado está exigindo.
    => Executado, inclusive por isso o código ficou pequeno e limpo.

## Exercícios que eu executei na primeira vez

__SOLUTION 1__
`def verbing(s):`
    # +++ SUA SOLUÇÃO +++

    if 'ing' in s and len(s) > 3:
        result = s +'ly'

    if not 'ing' in s and len(s) > 3:
        result = s + 'ing'

    if len(s) < 3:
        result = s

    return result
