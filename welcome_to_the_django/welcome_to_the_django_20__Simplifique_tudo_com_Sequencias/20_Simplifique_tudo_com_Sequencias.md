# AULA 20

INFO => O conceito de sequencias

Strings, além de objetos, são uma sequencia de letras

TODO:
todo => O que é um char?

tamanho da string => len(variavel)

## SEQUENCIA

In: nome = 'Henrique'

Out:
      0  1  2  3  4  5  6  7
      H  e  n  r  i  q  u  e
     -8 -7 -6 -5 -4 -3 -2 -1

### EXEMPLOS

string[start stop step]

In: nome = 'Henrique'

In: len(nome)
Out:
     8

In: nome[2]
Out:
     'n'

In: nome[1]
Out:
     'e'

In: nome[8]
Out:
     `---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[5], line 1
----> 1 nome[8]

IndexError: string index out of range`

In: nome[len(nome) - 1]
Out:
     'e'

In: nome[-1]
Out:
     'e'

In: nome[::-1]
Out:
     'euqirneH'

In: nome[1:-1]
Out:
     'enriqu'

In: nome[1:]
Out:
     'enrique'

In: nome[1:]
Out:
     'enrique'

In: nome[:2]
Out:
     'He'

In: nome[::2]
Out:
     'Hniu'

In: len
Out:
     <function len(obj, /)>

### POR DEBAIXO DOS PANOS

(Protocolo)
len(nome) == nome.__len__() =>
>>> Nunca acesse diretamente um item com dunder (direto no python, porque o dunder demonstra que faz parte do protocolo da linguagem)

### outro ex

In: `pi = 3.14`

In: `pi.__len__()`
Out:
`---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[14], line 25
     22 len
     24 pi = 3.14
---> 25 pi.__len__()

AttributeError: 'float' object has no attribute '__len__'`

In: `len(pi)`
Out:
`---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[15], line 26
     24 pi = 3.14
     25 # pi.__len__()
---> 26 len(pi)

TypeError: object of type 'float' has no len()`
>>> Dessa maneira o erro é muito mais declarativo, nos dando mais claresa do erro em si.

## PARA VERIFICARMOS QUE ISSO REALMENTE É UM PROTOCOLO

In: nome[0] => (Açúcar sintático, traduz o acesso ao método do protocolo implementado)
Out:
     'H'

é a mesma coisa que:

In: nome.__getitem__(0)
Out:
     'H'

Assim como:

In: nome[1:-1:2]
Out:
     'erq'

é a mesma coisa que:
In: index = slice(1, -1, 2)

In: type(index) => index é um slice...
Out:
     slice

In: nome[index]
Out:
     'erq'

In: index. => ...  e tem alguns atributos:
Out:
     index.indeces  index.start  index.stop  index.step

In: index.indeces?
Out:
     `
Docstring:
S.indices(len) -> (start, stop, stride)

Assuming a sequence of length len, calculate the start and stop
indices, and the stride length of the extended slice described by
S. Out of bounds indices are clipped in a manner consistent with the
handling of normal slices.
Type:      builtin_function_or_method` => Essa função normaliza o slice

In: index
Out:
     slice(1, -1, 2)

In: index.indices(len(nome))
Out:
     (1, 7, 2) => normaliza o slice em função do número da sequencia

Por debaixo dos panos, seria o seguinte:
In: nome.__getitem__(slice(1, -1, 2))
Out:
     'erq'

Todas essas notações funcionam com qualquer objeto que tenha o protocolo de sequencia.
