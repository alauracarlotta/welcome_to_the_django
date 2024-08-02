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

In [7]: range(8)
Out[7]: range(0, 8) => Retorna um range object

In [8]: r = range(8)

In [9]: r[0]
Out[9]: 0

In [10]: r[1]
Out[10]: 1

In [11]: r[5]
Out[11]: 5

In [12]: r[8]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[12], line 1
----> 1 r[8]

IndexError: range object index out of range

In [13]: r[-1]
Out[13]: 7

In [14]: list(r) => __Passo o range para uma lista e assim verifico todos os números do range__
Out[14]: [0, 1, 2, 3, 4, 5, 6, 7] => O range produz programaticamente, gera somente quando acessamos ele.

Suponhamos que eu queira uma lista com 1.000.000 de numeros. Isso ocuparia muito espaço em memória, mas utilizando o range, eu ocuparia somente um espaço em memória, podendo acessá-lo quando eu quiser de qualquer forma.

In [15]: range? => __documentação__
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

In [16]: range(1, 20, 3)
Out[16]: range(1, 20, 3) => Retorna o objeto, mas se colocarmos numa lista... 

In [17]: list(range(1, 20, 3))
Out[17]: [1, 4, 7, 10, 13, 16, 19] => ... retorna a sequencia

Melhorando ainda, vemos:

In: for letra in nome:
        print(letra)

Out:
L
a
u
r
a

Enumerate retorna uma tupla com índice e caracter:

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
In [21]: enumerate('Laura')
Out[21]: <enumerate at 0x7e16220027f0>
Ele retorna um interador que é o objeto enumerate
