
""" 
    ¹NOTE =>
    Qual é a primeira coisa que o python lê?
    Se você disse 'é a função main()', ERROU
        => Em C o entre ponto do programa é o __main__,
        em python é o módulo, o arquivo inteiro, o file .py!
        
        Entre ponto do python, sempre será o nome do arquivo executado!
        Se executarmos só python3, o interpretador do python cria um módulo vazio 
        e qualquer coisa que nós definirmos será no namespace do módulo.
        
        Com a função built-in do python 'globals()' conseguimos ver todas as variáveis globais
        
    ²NOTE =>
        Variáveis dentro de funções são variáveis 'LOCAIS'
    
    ³NOTE =>
        Toda vez que vermos algo com o dunder (ex.: __name__), significa que estamos acessando uma coisa interna do python
        da fronteira entre o código do usuário (dev) e os códigos internos do python
    
    TODOs:
    ========>
    * todo Entender melhor sobre variáveis globais no python
    * todo O que é esse namespace  do python (zen do python)
"""


"""
    VARIÁVEIS GLOBAIS = [
        os,
        main,
        foo,
        __name__
    ]
"""

"""
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
"""

import os


def main(): # NOTE¹
    print('Hello world!')
    print("This is Alice's greeting.")
    print('This is bob\'s greeting.')

    foo(5, 10)

    print('=' * 10)
    text = 'The current working directory is ' # NOTE²
    print(text + os.getcwd())

    foods = ['apples', 'oranges', 'bananas']

    for food in foods:
        print('I like to eat ', food)

    print('Count to ten: ')
    for i in range(1, 11):
        print(i)


def foo(a, b):
    """sumary_line
        função que soma dois valores.

    Keyword arguments:
    a: recebe um valor inteiro ou real
    b: recebe um valor inteiro ou real
    Return: retorna a soma de a + b
    """
    
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

if __name__ == '__main__': # NOTE³
    main()
