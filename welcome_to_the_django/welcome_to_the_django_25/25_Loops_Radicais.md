# Aula 25

INFO => Falando sobre loops (For e While)

NOTE¹ = lOOPS

In: nome = 'Laura'
In: print(nome, len(nome))
Out: Laura 5

In: i = 0
In: while i < 5:
        print(nome[i])
        i = i + 1
Out:
L
a
u
r
a

Melhorando o código:

In: while i < len(nome):
        print(nome[i])
        i += 1
Out:
L
a
u
r
a

Sempre que você tem um loop que precisa contar quantos passos ele vai dar, quantas vezes ele vai executar o corpo do loop, é melhor usar o __for__.

In: for i in range(len(nome)): => __range__ (trabalha com intervalo) NOTE²
        print(nome[i])
Out:
L
a
u
r
a

NOTE² =>

In: range(8)
Out: range(0, 8) => Retorna um range object

In: r = range(8)

In: r[0]
Out: 0

In: r[1]
Out: 1

In: r[5]
Out: 5

In: r[8]
`---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[12], line 1
----> 1 r[8]

IndexError: range object index out of range`

In: r[-1]
Out: 7

In: list(r) => __Passo o range para uma lista e assim verifico todos os números do range__
Out: [0, 1, 2, 3, 4, 5, 6, 7] => O range produz programaticamente, gera somente quando acessamos ele.

Suponhamos que eu queira uma lista com 1.000.000 de numeros. Isso ocuparia muito espaço em memória, mas utilizando o range, eu ocuparia somente um espaço em memória, podendo acessá-lo quando eu quiser de qualquer forma.

In: range? => __documentação__
Init signature: range(self, /, *args, **kwargs)
Docstring:
range(stop) -> range object
range(start, stop[, step]) -> range object (*Da mesma maneira como funciona o slice*)

Return an object that produces a sequence of integers from start (inclusive)
to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
These are exactly the valid indices for a list of 4 elements.
When step is given, it specifies the increment (or decrement).
Type:           type
Subclasses:

In: range(1, 20, 3)
Out: range(1, 20, 3) => Retorna o objeto, mas se colocarmos numa lista... 

In: list(range(1, 20, 3))
Out: [1, 4, 7, 10, 13, 16, 19] => ... retorna a sequencia

Melhorando ainda, vemos:

In: for letra in nome:
        print(letra)

Out:
L
a
u
r
a

__Enumerate retorna uma tupla com índice e caracter:__

In: for letra in enumerate(nome):
        print(letra)

Out:
(0, 'L') => (índice, valor)
(1, 'a')
(2, 'u')
(3, 'r')
(4, 'a')

Podendo usar assim:

In: for indice, letra in enumerate(nome):
        print(indice, letra)
Out:
0 L
1 a
2 u
3 r
4 a

Se fizermos:
In: enumerate('Laura')
Out: <enumerate at 0x7e16220027f0>
Ele retorna um interador que é o objeto enumerate

Todo iterador implementa o __next__

In: e = enumerate('Laura')

In: e
Out: <enumerate at 0x7f28a695c180>

In: next(e)
Out: (0, 'L')

In: next(e)
Out: (1, 'a')

In: next(e)
Out: (2, 'u')

In: next(e)
Out: (3, 'r')

In: next(e)
Out: (4, 'a')

In: next(e)
`---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
Cell In[9], line 1
----> 1 next(e)` => __Esse next é tratado pelo for no loop (for it)__

In: for indice, letra in enumerate(nome):
        if letra == 'a':
            continue => __O 'continue' fará com que pulemos a condicional__
        print(indice, letra)

Out:
0 L
2 u
3 r

Caso eu queira interromper a execução, utilizo *'break'*:

In: for indice, letra in enumerate(nome):
        if letra == 'r':
            break
        print(indice, letra)

Out:
0 L
1 a
2 u
