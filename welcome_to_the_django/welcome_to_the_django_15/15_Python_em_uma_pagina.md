# AULA 15

INFO => Entendendo o entry point de um file python

¹NOTE =>
Qual é a primeira coisa que o python lê?
Se você disse 'é a função main()', ERROU
    => Em C o 'entry point'* (docs/dict.md) do programa é o __main__,
    em python é o módulo, o arquivo inteiro, o file .py!

    Entre ponto do python, sempre será o nome do arquivo executado!
    Se executarmos só python3, o interpretador do python cria um módulo vazio 
    e qualquer coisa que nós definirmos será no 'namespace'* (docs/dict.md) do módulo.

    Com a função built-in do python 'globals()' conseguimos ver todas as variáveis globais.

---

²NOTE => Variáveis dentro de funções são variáveis 'LOCAIS'.

---

³NOTE => Toda vez que vermos algo com o dunder (ex.: __name__), significa que estamos acessando uma coisa interna do python
    da fronteira entre o código do usuário (dev) e os códigos internos do python

---

⁴NOTE => Todo módulo também é um objeto. Ao fazer type(os), o python te dará o tipo, module. Quando o python importa o modulo, ele cacheia ele e sempre que formos usá-lo ele irá buscar no cachê áquilo que já referenciamos.

---

⁵NOTE => Use os.getcwd() para ver o caminho do path

TODO:
=====>
>> todo Entender melhor sobre variáveis globais no python \
>> todo O que é esse namespace  do python (zen do python)

---

    VARIÁVEIS GLOBAIS = [
        os,
        main,
        foo,
        __name__
    ]

---

    VARIÁVEIS LOCAIS = {
        main: [
            text,
            food,
            i
        ],
        foo: [
            value
        ]
    }

---

`import os` # NOTE⁴ NOTE⁵

`def main():` # NOTE¹ \

    print('Hello world!')
    print("This is Alice's greeting.")
    print('This is bob\'s greeting.')

    `foo(5, 10)`

    print('=' * 10)
    text = 'The current working directory is ' # NOTE²
    print(text + os.getcwd())

    foods = ['apples', 'oranges', 'bananas']

    for food in foods:
        print('I like to eat ', food)

    print('Count to ten: ')
    for i in range(1, 11):
        print(i)`

`def foo(a, b):`

    value = a + b

    print('%s plus %s is equal to %s' % (
        a, b, value))

    if value < 50:
        print('foo')
    elif (value >= 50) and \
        ((a == 42) or (b == 24)):
        print('bar')
    else:
        print('moo')

    """ A multi-
    line string, but can also be a 
    multi-line comment. """

    return value # This is a one-line comment

`if __name__ == '__main__':` # NOTE³ \

    main()
