# AULA 23

INFO => Dicionários são hash-maps - armazenam chave/valor. (As chaves precisam ser objetos imutáveis, já os valores podem ser MUTÁVEIS).

## Exemplo

In: usuario = {
        'nome': 'Laura',
        'cidade': 'Jundiaí',
        'brasileira': True,
        'idade': 30,
        'peso': 76,
        'altura': 1.64
    }

In: usuario
Out:
{'nome': 'Laura',
 'cidade': 'Jundiaí',
 'brasileira': True,
 'idade': 30,
 'peso': 76,
 'altura': 1.64}

In: usuario['nome']
Out: 'Laura'

In: usuario['nome'] = 'Laura Carlota'

In: usuario
Out:
{'nome': 'Laura Carlota',
 'cidade': 'Jundiaí',
 'brasileira': True,
 'idade': 30,
 'peso': 76,
 'altura': 1.64}

>>> Para saber se há uma chave x no dicionário:

In: 'raca' in usuario
Out: False

>>> Para saber se há um valor x no dicionário:

In: 30 in usuario.values()
Out: True

>>> Para saber se há uma chave x no dicionário:

In: usuario.get('raca')

In: print(usuario.get('raca'))
None

>>> Podemos passar o segundo parâmetro ao get e assim ao invés de retornar __None__, Retornará o valor passado.

In: usuario.get('raca', 'valor x')
Out: 'valor x'

In: len(usuario)
Out: 6 => __Retorna a quantidade de chaves do dicionário__

In: usuario.keys() => __Retorna as chaves existentes__
Out: dict_keys(['nome', 'cidade', 'brasileira', 'idade', 'peso', 'altura'])

In: usuario.values() = __Retorna os valores existentes__
Out: dict_values(['Laura Carlota', 'Jundiaí', True, 30, 76, 1.64])

In: usuario.items() => __Retorna um dictionar-view (ou dict-view) com chave e valor existentes__
Out: dict_items([('nome', 'Laura Carlota'), ('cidade', 'Jundiaí'), ('brasileira', True), ('idade', 30), ('peso', 76), ('altura', 1.64)])

In: chave = usuario.keys()

In: valor = usuario.values()

In: items = usuario.items()

In: chave
Out: dict_keys(['nome', 'cidade', 'brasileira', 'idade', 'peso', 'altura'])

In: valor
Out: dict_values(['Laura Carlota', 'Jundiaí', True, 30, 76, 1.64])

In: items
Out: dict_items([('nome', 'Laura Carlota'), ('cidade', 'Jundiaí'), ('brasileira', True), ('idade', 30), ('peso', 76), ('altura', 1.64)])

In: usuario['Olá'] = 'Mundo'

In: usuario
Out:
{'nome': 'Laura Carlota',
 'cidade': 'Jundiaí',
 'brasileira': True,
 'idade': 30,
 'peso': 76,
 'altura': 1.64,
 'Olá': 'Mundo'}

In: chave
Out: dict_keys(['nome', 'cidade', 'brasileira', 'idade', 'peso', 'altura', 'Olá'])

In: chave = tuple(usuario.keys())

In: chave
Out: ('nome', 'cidade', 'brasileira', 'idade', 'peso', 'altura', 'Olá')

>>> Para deletar um item é através da chave, podendo ser através do del ou .pop()

In: del usuario['Olá']

In: usuario
Out:
{'nome': 'Laura Carlota',
 'cidade': 'Jundiaí',
 'brasileira': True,
 'idade': 30,
 'peso': 76,
 'altura': 1.64}

In: usuario.pop('brasileira')
Out: True

In: usuario
Out:
{'nome': 'Laura Carlota',
 'cidade': 'Jundiaí',
 'idade': 30,
 'peso': 76,
 'altura': 1.64}

>>> Como as chaves são imutáveis, o interpretador estoura o erro:
In: lista = [1, 'abacaxi', 'zebra']

In: usuario[lista] = 'Pode?'

Out:
`---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[33], line 1
----> 1 usuario[lista] = 'Pode?'

TypeError: unhashable type: 'list'`

In: hash(lista)

Out:
`---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[34], line 1
----> 1 hash(lista)

TypeError: unhashable type: 'list'`

In: hash((1,2))
Out: -3550055125485641917

In: hash('Laura')
Out: -19500349123424279

>>> Já os valores podem receber e serem alterados a qualquer hora.
In: usuario.update(interesses=['Patins', 'Leitura', 'Costurar'])

In: usuario
Out:
{'nome': 'Laura Carlota',
 'cidade': 'Jundiaí',
 'brasileira': True,
 'idade': 30,
 'peso': 76,
 'altura': 1.64,
 'interesses': ['Patins', 'Leitura', 'Costurar']}

In: usuario['interesses'].append('Tatuagens')

In: usuario
Out:
{'nome': 'Laura Carlota',
 'cidade': 'Jundiaí',
 'brasileira': True,
 'idade': 30,
 'peso': 76,
 'altura': 1.64,
 'interesses': ['Patins', 'Leitura', 'Costurar', 'Tatuagens']}

In: minha_tupla = tuple(usuario.items())

In: minha_tupla
Out: => __Uma tupla de tuplas__
(('nome', 'Laura Carlota'),
 ('cidade', 'Jundiaí'),
 ('idade', 30),
 ('peso', 76),
 ('altura', 1.64),
 ('interesses', ['Patins', 'Leitura', 'Costurar', 'Tatuagens']))

In: dict(minha_tupla)
Out: => __Transforma novamente a tupla num dicionário__
{'nome': 'Laura Carlota',
 'cidade': 'Jundiaí',
 'idade': 30,
 'peso': 76,
 'altura': 1.64,
 'interesses': ['Patins', 'Leitura', 'Costurar', 'Tatuagens']}

>>> Podemos criar de forma direta:
In: dict(nome='Maggie', idade=10, raca='srd')
Out: {'nome': 'Maggie', 'idade': 10, 'raca': 'srd'}

dictionar-view
