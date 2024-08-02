# AULA 24

INFO => Em tempo de execução, o python verifica os tipos.

Em python podemos declarar da seguinte forma:
`letras = 'abc'`

Já em C, seria necessário inicializar com algo como:
`char letras = 'abc';`

Como o python sabe como aplicar, por exemplo, letras.upper()? Como ele sabe que o .upper() conseguirá ser aplicado em letras?

Primeiro ele verifica ao que o método está associado;

In: `letras`
Out: 'abc'

Ele entende que o método está associado ao objeto do tipo string

In: letras.upper
Out: <function str.upper()>

e com o assessor (na linguagem python é o ponto(.)) ele pergunta pelo método upper no objeto string referenciado em letras.

E agora que ele sabe qual é o método, ele pode aplicar o executador () para executar o método.

In: letras.upper()
Out: 'ABC'

>>> Dinâmicamente ele descobriu o tipo do objeto, os seus componentes e executou o método. Isso é tipagem dinâmica em ação.

## A tipagem em python é forte

Ou seja, ele não fica convertendo os seus objetos em outro implicitamente. Ex:

In:
`1 + '1'`
`---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[21], line 1
----> 1 1 + '1'

TypeError: unsupported operand type(s) for +: 'int' and 'str'`

>>> Com isso, eo preciso decidir se eu quero somar dois numeros ou concatenar as strings:

In: 1 + int('1') NOTE¹
Out: 2

ou

In: str(1) + '1' NOTE²
Out: '11'

NOTE¹ NOTE² = Açúcar sintático (ou magic methods), por debaixo dos panos, o python está fazendo o seguinte:

In: '1'.__add__(str(1)) => *Concatena*
Out: '11'

In: int('1').__add__(1) => *Soma*
Out: 2

In: 3 * 42
Out: 126

In: '#' * 42
Out: '##########################################'

In: '#'.__mul__(42) => *Repetição*
Out: '##########################################'

In: int(3).__mul__(42) => *Multiplica*
Out: 126

É o tipo que define a semantica do operador.
Esse detalhes são implementados nas classes e nós podemos implementar isso nas nossas classes também para que o uso da sobrecarga dos operadores nos sejam úteis assim como para simplificar o código.

In: 3 % 2
Out: 1

In: int(3).__mod__(2)
Out: 1

In: 'Olá,  %s!' % 'Henrique'
Out: 'Olá,  Henrique!' => Ele coloca a segunda string, no espaço (nesse placeholder) por cento da primeira string.

>> Outro exemplo:

In: 'Olá,  %s! %s' % ('Henrique', 'Bom dia!')
Out: 'Olá,  Henrique! Bom dia!'

In: 'Olá,  %s! %s'.__mod__(('Henrique', 'Bom dia!'))
Out: 'Olá,  Henrique! Bom dia!'
