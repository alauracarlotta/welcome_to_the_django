# Aula 26

INFO => Expresões regulares

nome = 'Laura'

In: for cont in nome:
        print(cont)

Out:
L
a
u
r
a

In: for cont in nome:
        if cont == 'a' or cont == 'u':
            print(cont.upper())
        print(cont)

Out:
L
A
a
U
u
r
A
a

In: for cont in nome:
        if cont == 'a' or cont == 'u':
            print(cont.upper())
            continue
        print(cont)

Out:
L
A
U
r
A

In: for cont in nome:
        if cont == 'a' or cont == 'u':
            print(cont.upper())
        else:
            print(cont)

Out:
L
A
U
r
A

In: for cont in nome:
        if cont in ('a', 'u'):
            print(cont.upper())
            continue
        print(cont)

Out:
L
A
U
r
A

In: for cont in nome:
        if cont in 'au':
            print(cont.upper())
            continue
        print(cont)

Out:
L
A
U
r
A

In: for cont in nome:
        if cont in 'aeiou':
            print(cont.upper())
        elif cont == 'r':
            print('@')
        else:
            print(cont)

Out:
L
A
U
@
A

## Verificando

`True and True`  == *True*
`True and False` == *False*
`True or True`   == *True*
`True or False`  == *True*

true e false são singletons do python (só existe uma instancia deles na linguagem), no enteanto todo objeto em python tem uma representação lógica

In: bool(None)
Out: False

In: bool(False)
Out: False

In: bool(0)
Out: False

In: bool('')
Out: False

In: bool(())
Out: False

In: bool([])
Out: False

In: bool({})
Out: False

>>> curto cirquito => Ele avalia sempre o caminho menor sob a devida avaliação

In: bool({})
Out: False

In: bool(True)
Out: True

In: bool(['abc'])
Out: True

In: True and 'abc'
Out: 'abc'

In: True or 'abc'
Out: True

In: 'abc' or True
Out: 'abc'

In: 'abc' and True
Out: True

In: [] and True
Out: [] => __Para que o and seja 'True' ele precisa que as duas expressões sejam True, quando ele verifica a lista vazia que é falsa ele nem avalia o segundo elemento e retornando assim a lista vazia []__

>>> O avaliador sempre retorna o ultimo elemento avaliado

In: [] and True
Out: []

In: 1 and indefinido
`---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[27], line 1
----> 1 1 and indefinido

NameError: name 'indefinido' is not defined`

In: 1 or indefinido
Out: 1
