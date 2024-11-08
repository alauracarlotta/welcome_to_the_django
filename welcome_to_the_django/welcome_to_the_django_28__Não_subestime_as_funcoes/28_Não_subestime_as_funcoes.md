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
In: def f():
        pass

In: print(f())
Out:
    None => __Ela retorna *NONE* porque toda função em python, retorna alguma coisa. E se você não explicitar, ela sempre irá retornar NONE.__ __(O python não tem 'void')__

>>> Funções em python também recebem argumentos:
In: def f(a, b, c):
        print(a, b, c) __=> Essa forma de passar parâmetros, se chama parâmetros posicionais, onde a ordem dos parâmetros vão bater com a ordem dos argumentos.__

In: f('A', 'B', 'C')
Out:
    A B C

>>> Podendo ter também parâmetros nomeados:
In: f(a = 'A', b = 'B', c = 'C')
Out:
    A B C

In: f(c = 'C', b = 'B', a = 'A') __=> Neste caso, a ordem não importará__
Out:
    A B C

>>> Podemos declarar funções como parâmetros default:
In: def f(a, b, c = 'E'):
        print(a, b, c)
>>> E no caso de não passarmos os argumentos, estourará o seguinte erro:
In: f()
`---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[13], line 1
----> 1 f()

TypeError: f() missing 2 required positional arguments: 'a' and 'b'`

>>> Passando os argumentos 'a' e 'b', tendo o c como default, a chamad a seguir printa áquilo que já era esperado:
In: f('l', 'i')
Out:
    l i E
>>> Parâmetros posicionais indefinidos:
>>> Como convenção utilizamos o asterisco [*] e args (e os args sempre estarão numa tupla com os valores correspondentes)

In: def f(a, b, c = 'E', *args):
        print(a, b, c, args)

In: f('l', 'i', 2, True)
Out:
    l i 2 (True,)

In: f('l', 'i', 2, True, [], 'banana', -14.5)
Out:
    l i 2 (True, [], 'banana', -14.5)

>>> O python também suporta receber n argumentos nomeados, da seguinte forma:
In: def f(a, b, c = 'E', **kwargs): __=> Com dois *s nomeado 'kwargs'__
        print(a, b, c, kwargs)

In: f('l', 'i', c = 'c', numero = 2, booleano = True, lista = [], fruta = 'banana', temperatura = -14.5)
Out:
    l i c {'numero': 2, 'booleano': True, 'lista': [], 'fruta': 'banana', 'temperatura': -14.5} __=> O que nos retorna um dicionário com chave e valor referenciado pelo kwargs.__

In: f(a = 'a', b = 'b', l = 'l', i = 'i', c = 'c', numero = 2, booleano = True, lista = [], fruta = 'banana', temperatura = -14.5)
Out:
    a b c {'l': 'l', 'i': 'i', 'numero': 2, 'booleano': True, 'lista': [], 'fruta': 'banana', 'temperatura': -14.5}

>>> Exemplo do erro com argumentos duplicados:
In: f(a = 'a','B', b = 'b', l = 'l', i = 'i', c = 'c', numero = 2, booleano = True, lista = [], fruta = 'banana', temperatura = -14.5)

Out:
    `Cell In[28], line 1
    f(a = 'a','B', b = 'b', l = 'l', i = 'i', c = 'c', numero = 2, booleano = True, lista = [], fruta = 'banana', temperatura = -14.5)
                                                                                                                                     ^
    SyntaxError: positional argument follows keyword argument`

>>> Podemos misturar o *args e o **kwargs
In: `def f(a, b, c = 'E', *args, **kwargs):
        print(a, b, c, args, kwargs)`

In: f('a', 'b', 'c', 'd', 'e', f = 'f', w = 'w')
Out:
    a b c ('d', 'e') {'f': 'f', 'w': 'w'}

In: def f(a, b, c = 'E', *args, x, y, **kwargs):
        print(a, b, c, x, y, args, kwargs) __keyword-only argument, argumento que obrigatoriamente eu devo passar nomeado, adicionando-o entre o *args e o **kwargs__

>>> Exemplo de erro:
In: f('a', 'b', 'c', 'd', 'e', f = 'f', w = 'w')
Out:
    `---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    Cell In[45], line 1
    ----> 1 f('a', 'b', 'c', 'd', 'e', f = 'f', w = 'w')

    TypeError: f() missing 2 required keyword-only arguments: 'x' and 'y'`

In: f('a', 'b', 'c', 'd', 'e', f = 'f', w = 'w', x=1, y=0)
a b c 1 0 ('d', 'e') {'f': 'f', 'w': 'w'}
>>> Esse recurso é legal para usarmos por exemplo como parâmetros de configuração, onde você explicita qual argumentação você está usando na chamada. Faz muito sentido usar esses caras quando você tem valores default para usar.
>>> Isso é útil para explicitar uma mudança no comportamento da função, exigindo que o usuário da função passe o parâmetro nomeado, facilitando a leitura.

## O django usa o kwargs na função FILTER

In: def filter(**lookups): __O filter usa 'lookups' ao invés de kwargs__
        for k, v in lookups.items():
            print(k.split('__'), v)

In: filter(
            name__startswith='Hen',
            age__lt=30,
            city__endswith='rói'
            )
Out:
    ['name', 'startswith'] Hen
    ['age', 'lt'] 30
    ['city', 'endswith'] rói

In: filter(
            name__startswith='La',
            age__lt=30,
            city__endswith='ulo'
            )
Out:
    ['name', 'startswith'] La
    ['age', 'lt'] 30
    ['city', 'endswith'] ulo
__Como todos esses parâmetros vão estar dentro do lookups, que é um dicionário, eu tenho chave e valor, ou seja, eu consigo usar o '.items()', eu consigo percorreo dicionário lookups item a item (com o .items()), que vai me retornar uma tupla colocando chave (k) e valor (v), então eu separo a chave com o split usando o double underscore, então temos o campo 'age' com a operação menor que 'lt' e o valor 30, temos 'name' com a operação startswith com o valor Hen, 'city' com a operação 'endswith' com valor 'rói' e assim o django consegue alimentar o maquinário do ORM e gerar as qwerys pra gente usando a api do python__

## Temos o formato mais genérico possível

In: def f(*args, **kwargs):
        print(args, kwargs)

In: f('a', 'b', 'c', 'd', 'e', 2, 5, f = 'f', w = 'w', boolean = False)
Out:
    ('a', 'b', 'c', 'd', 'e', 2, 5) {'f': 'f', 'w': 'w', 'boolean': False}

>>> Separando e colocando os valores nas variáveis...
In: t = 'a', 'b', 'c'

In: d = dict(f = 'f', w = 'w', boolean = False)

In: print(t, d)
Out:
    ('a', 'b', 'c') {'f': 'f', 'w': 'w', 'boolean': False}

>>> ... Vemos que o args recebe os dois valores (conseguimos ver isso pois os valores estão envolvidos numa tupla), enquanto para o kwargs, vemos que o valor está vazio (como demonstram as chaves vazias do print)

In: f(t, d)
Out:
    (('a', 'b', 'c'), {'f': 'f', 'w': 'w', 'boolean': False}) {}

>>> Dessa maneira precisamos explicitar da seguinte forma:
In: f(t[0], t[1], t[2], f=d['f'], w=d['w'], boolean=d['boolean'])
Out:
    ('a', 'b', 'c') {'f': 'f', 'w': 'w', 'boolean': False}
__Essa forma não é nada 'pythonica', com isso, podemos fazer o unpacking da tupla e do dicionário com os parâmetros dessa função__

In: f(*t, **d)
Out:
    ('a', 'b', 'c') {'f': 'f', 'w': 'w', 'boolean': False}

## As belas funções

In: add
Out:
    <function __main__.add(a, b)>

In: type(add)
Out:
    function

>>> Como funções também são objetos, logo, uma função tem atributos
In: add.__code__
Out:
    <code object add at 0x70d988108b90, file `"<ipython-input-17-b2d6d05c6b17>"`, line 1> __Isso é um 'objeto código'__
>>> Quantos argumentos existem na criação da função

In: add.__code__.co_argcount
Out:
    2

>>> Os bytes que o python gera para criar a função

In: add.__code__.co_code
Out:
    b'\x97\x00|\x00|\x01z\x00\x00\x00S\x00'

>>> O nome da função

In: add.__code__.co_name
Out:
    'add'

>>> Quais são as variáveis locais dessa função

In: add.__code__.co_varnames
Out:
    ('a', 'b')

In: import dis => __Que é o dis assembly__

In: dis.dis(add)
  1           0 RESUME                   0

  2           2 LOAD_FAST                0 (a) => __mostra a instrução carregada pelo python__
              4 LOAD_FAST                1 (b)
              6 BINARY_OP                0 (+)
             10 RETURN_VALUE

>>> Podemos criar a documentação da função
In: def add(a, b):
        'soma a + b'
        return a + b

In: add.__doc__
Out:
    'soma a + b'

In: help(add)
Out:
Help on function add in module __main__:
    add(a, b)
        soma a + b
    (END)

>>> Assim podemos criar outro exemplo:
In: def calc(op, a, b):
        return op(a, b)

In: calc(add, 3, 9)
Out:
    12

In: def mul(a, b):
        return a * b

In: calc(mul, 3, 9)
Out:
    27
