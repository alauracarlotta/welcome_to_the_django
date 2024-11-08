# AULA 19

INFO => Entendendo as strings

As 3 formas de declarar strings:
    `print('Hello world!')`
    `print("This is Alice's greeting.")`
    `print('This is bob\'s greeting.')`

No python, strings também são objetos!

TODO:
todo => O que é algo unicode?

No Python todas as strings são unicode* docs/dict.md (Não é uma sequencia de bytes como em C, por exemplo. É um objeto de alto nível que implementea o unicode e é preciso fazer o encoding dele pra bytes para transmitir na rede ou guardar em um arquivo, por ex.) -> padrão UTF-8

EX:

In: 'henrique'.encode()
Out: b'henrique'

In: 'henriquê'.encode()
Out: b'henriqu\xc3\xaa'

In: 'henriquë'.encode()
Out: b'henriqu\xc3\xab'

In: 'HƐƞ®ɪǫưΣ'.encode()
Out: b'H\xc6\x90\xc6\x9e\xc2\xae\xc9\xaa\xc7\xab\xc6\xb0\xce\xa3'

Strings no Python, são imutáveis, ou seja, para alterá-la, você precisará atrubuí-la a uma variável

Veja:
nome.capitalize()    nome.ljust()
nome.casefold()      nome.lower()
nome.center()        nome.lstrip()
nome.count()         nome.maketrans()
nome.encode()        nome.partition()
nome.endswith()      nome.removeprefix()
nome.expandtabs()    nome.removesuffix()
nome.find()          nome.replace()
nome.format()        nome.rfind()
nome.format_map()    nome.rindex()
nome.index()         nome.rjust()
nome.isalnum()       nome.rpartition()
nome.isalpha()       nome.rsplit()
nome.isascii()       nome.rstrip()
nome.isdecimal()     nome.split()
nome.isdigit()       nome.splitlines()
nome.isidentifier()  nome.startswith()
nome.islower()       nome.strip()
nome.isnumeric()     nome.swapcase()
nome.isprintable()   nome.title()
nome.isspace()       nome.translate()
nome.istitle()       nome.upper()
nome.isupper()       nome.zfill()
nome.join()

Ao invés de concatenar com o simbolo de adição, ex:
`'Laura' + ' ' + 'Carlota'`, gerando assim uma 4ª string, utilize o .join(). Ex: `' '.join(['Laura', 'Carlota])`

In:' '.join(['Laura', 'Carlota'])
Out: 'Laura Carlota'

In: '\n'.join(['Laura', 'Carlota'])
Out: 'Laura\nCarlota'

In: print('\n'.join(['Laura', 'Carlota']))
Out: Laura
     Carlota
