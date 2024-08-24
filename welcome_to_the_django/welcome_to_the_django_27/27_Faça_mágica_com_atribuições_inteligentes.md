# Aula 27

INFO => Atribuição a valores

In: row = 'Laura', 'SP', -23.54, -46.63

In: type(row)
Out: tuple

In: print(row)
('Laura', 'SP', -23.54, -46.63)

>>> Criando a função, podemos atribuir da seguinte maneira (convencional):
In: def f(t):
        nome = t[0]
        cidade = t[1]
        latitude = t[2]
        longitude = t[3]
        print(nome, cidade, latitude, longitude)

In: if __name__ == '__main__':
        f(row)
Out:
Laura SP -23.54 -46.63

>>> No python podemos atribuir vário valores de uma só vez
In: def f(t):
        nome, cidade, latitude, longitude = t[0], t[1], t[2], t[3]
        print(nome, cidade, latitude, longitude)

In: if __name__ == '__main__':
        f(row)
Out:
Laura SP -23.54 -46.63

>>> Contudo, se temos 4 variáveis e 4 elementos dentro da tupla, podemos declarar da forma a seguir:
In: def f(t):
        nome, cidade, latitude, longitude = t (__o python não é como o orkut: ELE SABE CONTAR__ KKKKKKKK)
        print(nome, cidade, latitude, longitude)

In: if __name__ == '__main__':
        f(row)
Out:
Laura SP -23.54 -46.63

>>> Se quisermos somente 'nome' e 'cidade', podemos atribuir dessa forma (convencional):
In: def f(t):
        nome, cidade = t[0], t[1]
        print(nome, cidade)

In: if __name__ == '__main__':
        f(row)
Out:
Laura SP

>>> Podemos atribuir com o slice:
In: def f(t):
        nome, cidade = t[:2]
        print(nome, cidade)

In: if __name__ == '__main__':
        f(row)
Out:
Laura SP

>>> Se eu quisesse somente 'nome' e 'longitude', poderia ser da forma convencional, ...
In: def f(t):
        nome, longitude = t[0], t[3]
        print(nome, longitude)

In: if __name__ == '__main__':
        f(row)
Out:
Laura -46.63

>>> (A melhor forma, no caso se quisermos o último elemento, deveria ser assim:)
In: def f(t):
        nome, longitude = t[0], t[-1]
        print(nome, longitude)

In: if __name__ == '__main__':
        f(row)
Out:
Laura -46.63

>>> ...Ou assim: O _ serve para nomearmos uma variável 'temporárea' (que não será usada novamente). Neste caso, estamos utilizando dois undercores porque sabemos a qtde de elementos e que queremos o 1º e o últimos elemento. Os demais não nos interessam:

In: def f(t):
        `nome, _, _, longitude = t`
        print(nome, longitude, _)

In: if __name__ == '__main__':
        f(row)
Out:
Laura -46.63 -23.54 *=> Aqui o print do _ fica como latitude pois o 2º _ sobrepõe o 1º.*

>>> Contudo, podemos usar o '*' para dizer - "todos os outros elementos que estiver entre o 1º e o último":
In: def f(t):
        `nome, *_, longitude = t
        print(nome, longitude, _)`

In: if __name__ == '__main__':
        f(row)
Out:
Laura -46.63 ['SP', -23.54]

In: def f(t):
        `nome, *meio, longitude = t` *=> Podemos nomear o asterisco ao invés de usar o underscore*
        print(nome, longitude, meio)

In: if __name__ == '__main__':
        f(row)
Out:
Laura -46.63 ['SP', -23.54]

>>> Outro exemplo:
In: def f(t):
        *nome, _, longitude = t
        `print(nome, longitude, _)`

In: if __name__ == '__main__':
        f(row)
Out:
['Laura', 'SP'] -46.63 -23.54

>>> Esse formato funcionar em qualquer parte do código:
In: `def f(t):
        *_, latitude, longitude = t
        print(latitude, longitude,_)`

In: if __name__ == '__main__':
        f(row)
Out:
-23.54 -46.63 ['Laura', 'SP']

>>> Assim como:
In: def f(t):
        `nome, *_ = t
        print(nome, _)`

In: if __name__ == '__main__':
        f(row)
Out:
Laura ['SP', -23.54, -46.63]

>>> Essa forma de atribuição também é iteravel:
In: table = (('Laura', 'SP', -23.54, -46.63),
             ('Henrique', 'Niteroi', 22.9, 54.7)
            )

In: `for row in table:
        nome = row[0]
        cidade = row[1]
        latitude = row[2]
        longitude = row[3]
        print(nome, cidade, latitude, longitude)`
Out:
Laura SP -23.54 -46.63
Henrique Niteroi 22.9 54.7

>>> Como mostrado no código anterior:
In: `for row in table:
        nome, cidade, latitude, longitude = row
        print(nome, cidade, latitude, longitude)`
Out:
Laura SP -23.54 -46.63
Henrique Niteroi 22.9 54.7

***

>>> Podemos eliminar o 'row' e atribuir direto no for:
In: `for nome, cidade, latitude, longitude in table:
        print(nome, cidade, latitude, longitude)`
Out:
Laura SP -23.54 -46.63
Henrique Niteroi 22.9 54.7

***

>>> E ainda seguindo as mesmas premissas, como mostra o exemplo:
In: `for nome, *_, longitude in table:
        print(nome, longitude,_)`
Out:
Laura -46.63 ['SP', -23.54]
Henrique 54.7 ['Niteroi', 22.9]
