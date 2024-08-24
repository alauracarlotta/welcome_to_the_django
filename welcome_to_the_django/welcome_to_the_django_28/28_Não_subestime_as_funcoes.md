# Aula 28

INFO => As lindas e belas funções!!!

>>> Sempre primeiro criaremos a função e depois a executaremos:
*Criação*
In: def f():
        return 42

*Chamada*
In: if __name__ == '__main__':
        print(f())
Out:
42

>>> Podemos criar uma função vazia:
In [6]: def f():
   ...:     pass
   ...: 

In [7]: print(f())
None => Ela retorna *NONE* porque toda função em python, retorna alguma coisa. E se você não explicitar, ela sempre irá retornar NONE. __(O python não tem 'void')__

>>> Funções em python também recebem argumentos:
In [8]: def f(a, b, c):
   ...:     print(a, b, c) => Essa forma de passar parâmetros, se chama parâmetros posicionais, onde a ordem dos parâmetros vão bater com a ordem dos argumentos.
   ...: 

In [9]: f('A', 'B', 'C')
A B C

>>> Podendo ter também parâmetros nomeados:
In [10]: f(a = 'A', b = 'B', c = 'C')
A B C

In [11]: f(c = 'C', b = 'B', a = 'A') => Neste caso, a ordem não importará
A B C

>>> Podemos declarar funções como parâmetros default:
In [12]: def f(a, b, c = 'E'):
    ...:     print(a, b, c)
    ...: 

__E no caso de não passarmos os argumentos, estourará o seguinte erro:__
In [13]: f()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[13], line 1
----> 1 f()

TypeError: f() missing 2 required positional arguments: 'a' and 'b'

>>> Passando os argumentos 'a' e 'b', tendo o c como default, a chamad a seguir printa áquilo que já era esperado:
In [14]: f('l', 'i')
l i E

>>> Parâmetros posicionais indefinidos:
>>> Como convenção utilizamos o * e args (e os args sempre estarão numa tupla com os valores correspondentes)
In [15]: def f(a, b, c = 'E', *args):
    ...:     print(a, b, c, args)
    ...: 

In [16]: f('l', 'i', 2, True)
l i 2 (True,)

In [17]: f('l', 'i', 2, True, [], 'banana', -14.5)
l i 2 (True, [], 'banana', -14.5)

>>> O python também suporta receber n argumentos nomeados, da seguinte forma:
In [25]: def f(a, b, c = 'E', **kargs): __=> Com dois *s nomeado 'kargs'__
    ...:     print(a, b, c, kargs)
    ...: 

In [26]: f('l', 'i', c = 'c', numero = 2, booleano = True, lista = [], fruta = 'banana', temperatura
    ...:  = -14.5)
l i c {'numero': 2, 'booleano': True, 'lista': [], 'fruta': 'banana', 'temperatura': -14.5} __=> O que nos retorna um dicionário com chave e valor referenciado pelo kargs.__

In [27]: f(a = 'a', b = 'b', l = 'l', i = 'i', c = 'c', numero = 2, booleano = True, lista = [], fru
    ...: ta = 'banana', temperatura = -14.5)
a b c {'l': 'l', 'i': 'i', 'numero': 2, 'booleano': True, 'lista': [], 'fruta': 'banana', 'temperatura': -14.5}

>>> Exemplo do erro com argumentos duplicados:
In [28]: f(a = 'a','B', b = 'b', l = 'l', i = 'i', c = 'c', numero = 2, booleano = True, lista = [],
    ...:  fruta = 'banana', temperatura = -14.5)
  Cell In[28], line 1
    f(a = 'a','B', b = 'b', l = 'l', i = 'i', c = 'c', numero = 2, booleano = True, lista = [], fruta = 'banana', temperatura = -14.5)
                                                                                                                                     ^
SyntaxError: positional argument follows keyword argument

>>> Podemos misturar o *args e o **kargs
In [42]: def f(a, b, c = 'E', *args, **kwargs):
    ...:     print(a, b, c, args, kwargs)
    ...: 

In [43]: f('a', 'b', 'c', 'd', 'e', f = 'f', w = 'w')
a b c ('d', 'e') {'f': 'f', 'w': 'w'}

In [44]: def f(a, b, c = 'E', *args, x, y, **kwargs):
    ...:     print(a, b, c, x, y, args, kwargs) __keyword only argument, argumento que obrigatoriamente eu devo passar nomeado, adicionando-o entre o *args e o **kwargs__

>>> Exemplo de erro:
In [45]: f('a', 'b', 'c', 'd', 'e', f = 'f', w = 'w')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[45], line 1
----> 1 f('a', 'b', 'c', 'd', 'e', f = 'f', w = 'w')

TypeError: f() missing 2 required keyword-only arguments: 'x' and 'y'

In [46]: f('a', 'b', 'c', 'd', 'e', f = 'f', w = 'w', x=1, y=0)
a b c 1 0 ('d', 'e') {'f': 'f', 'w': 'w'}

WIP
TODO:
=> Parei em 7:16 min de vídeo.
