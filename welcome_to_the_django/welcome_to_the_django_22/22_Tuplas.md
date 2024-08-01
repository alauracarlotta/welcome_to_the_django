# AULA 22

INFO => Tuplas são sequencias não mutáveis.

In: ('A', 'B', 'C')
Out: ('A', 'B', 'C')

In: uma_tupla = ('A', 'B', 'C')

In: uma_tupla
Out: ('A', 'B', 'C')

In: type(uma_tupla)
Out: tuple

In: uma_tupla + ('D', 'E')
Out: ('A', 'B', 'C', 'D', 'E')

>>> Não existem muitos métodos em tuplas pois elas são imutáveis

In: uma_tupla.
              count() index()

In: uma_nova_tupla = uma_tupla + ('D', 'E')

In: uma_nova_tupla
Out: ('A', 'B', 'C', 'D', 'E')

In: uma_tupla, uma_nova_tupla
Out: (('A', 'B', 'C'), ('A', 'B', 'C', 'D', 'E'))

In: tuple?
Out:
`Init signature: tuple(iterable=(), /)
Docstring:
Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.
Type:           type
Subclasses:     int_info, float_info, UnraisableHookArgs, hash_info, version_info, flags, thread_info, asyncgen_hooks, _ExceptHookArgs, waitid_result, ...`

In [: tuple('Laura')
Out[: ('L', 'a', 'u', 'r', 'a')

In [: tuple([1, 2, 3])
Out[: (1, 2, 3)

In [: tuplaX = (1, 2.7, True, (2j, len), [4, 5, 6])

In [: tuplaX
Out[: (1, 2.7, True, (2j, <function len(obj, /)>), [4, 5, 6])

In [: print(tuplaX[2])
True

In [: tuplaX[2:]
Out[: (True, (2j, <function len(obj, /)>), [4, 5, 6])
