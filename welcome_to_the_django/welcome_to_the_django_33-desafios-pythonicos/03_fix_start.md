# FIX START

TODO:

* ✅ TODO usar o método replace
    => Usei em todas as 3 soluções que eu construí

* ✅ TODO usar outros métodos do python
    => Usei o método '.find()' para encontrar as letras iguais

* ✅ TODO escrever em apenas uma linha

    Metódo ternário:
        `<expressao1> if <condicao> else <expressao2>`

    Outra forma de simplificar:
        `('impar', 'par')[x%2==0]`

    Com isso, aprendi o método ternário com for e somente o if (sem else);
    Ex:
    In:
        `numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
        `pares = [x for x in numeros if x % 2 == 0]`
        `print(pares)`

    Out:
        `[2, 4, 6, 8, 10]`

## Contudo, há o que chamamos de 'LIST COMPREHENSION', que é o seguinte (e neste consiste o for com if-else)

    Metódo LIST COMPREHENSION:
        `<expressao1> if <condicao> else <expressao2> for <valor> in <lista>`
    In:
        `a = [a if a else 2 for a in [0,1,0,3]]`
        `print(a)`
    Out:
        `[2, 1, 2, 3]`

__=> Executado na solução 3.__

NOTE:

* Comentário HB:
  * Tentativa: Substitui e substitui de novo
  * Quantas ocorrencias aparecem daquela letra
  * Replace a partir do indice 1

=> Aprendizado: Eliminar repetições, legibilidade, nomear variáveis com nomes semanticos e pequenos

TODO:
[Ver 'FUNÇÕES ANÔNIMAS', (Comentado pelo WELL)](https://docs.python.org/pt-br/3/reference/expressions.html#lambda)
    Ex:
    a = lambda x : x*5

## Exercícios que eu executei na primeira vez

__SOLUTION 1__
`def fix_start(s):`
    return s[0] + s[1:].replace(s[0], '*') if len(s) > 1 else s

***

__SOLUTION 2__
`def fix_start(s):`
    new_string = ''
    for cont, value in enumerate(s):
        if cont == 0 or value != s[0]:
            new_string += value
        else:
            new_string += value.replace(s[0], '*')

    return new_string

***

__SOLUTION 3__
`def fix_start(s):`
    letter = s[0]
    new_word = ''
    for cont in range(len(s)):
        if s.find(letter, cont) and not cont == 0:
            new_word += s[cont].replace(letter, '*')
        else:
            new_word += s[cont]
        cont += 1
    return new_word
