# AULA 16

INFO => Ainda entendendo como módulos funcionam e como o entry point funciona.

¹NOTE => Todo módulo também é um objeto. Ao fazer type(os), o python te dará o tipo, module. Quando o python importa o modulo, ele cacheia ele e sempre que formos usá-lo ele irá buscar no cachê áquilo que já referenciamos.

---

²NOTE => Use os.getcwd() para ver o caminho do path => CWD - current working directoty

---

³NOTE => Use i comando In:`type(os)` => Out: <class 'module'>

---

⁴NOTE => Vide atributos que contem no os. Ex: In: os.__file__ => Out: '/usr/lib/python3.12/os.py' => (mostra o diretorio que originou esse arquivo)

---

In: import os as asdf (Estamos importando os com o nome asdf) \

In: asdf \
Out: <module 'os' (frozen)> \

In: xpto = asdf \

In: xpto \
Out: <module 'os' (frozen)> \

In: xpto.__file__ \
Out: '/usr/lib/python3.12/os.py' \

⁵NOTE => O mecaniosmo de import cria um objeto no ram time do python, é o interpretados que cuida desse objeto e no nosso namespace local nós só teremos uma variável que referencia esse objeto no ram time.

Então, acima, temos 3 variaveis que referenciam o mesmo objeto
In: os, asdf, xpto \
Out: (<module 'os' (frozen)>, <module 'os' (frozen)>, <module 'os' (frozen)>) \

In: id(os), id(asdf), id(xpto) \
Out: (135731018114976, 135731018114976, 135731018114976) \

=> Depois de encontrar o file, o python abre o arquivo texto, parseia todo o código-fonte do arquivo, gera os bitecodes e istancia o objeto modulo que referencia os bitecodes gerados. Assim o python gera um cash de todos os módulos que ele importa.

=> Como processar o código-fonte, gerar o bitecode todo, parsear o código e instanciar o módulo em memória é muito caro, se o usuário tentar importar o módulo mais de uma vez, o python irá buscar a primeira referencia que já está cacheada em memória. Não há diferença entre importar o moódulo todo ou apenas alguns recursos dele, já que uma vez processado (e mesmo usando o from, o python irá cachear o módulo todo), a única diferença é você não terá que ficar usando assessor (o .alguma_coisa) a todo momento no código, no caso de você usar apenas uma ou duas ferramentas do módulo.

---

⁶NOTE => É possível também importar apenas um recurso do módulo. Ex:
`from os import getcwd` e é como se fosse `from os import getcwd as getcwd` ou ainda podemos user da seguinte maneira: `from os import getcwd as xyz`

In: getcwd() \
Out: '/home/laura-carlotta/dev-projects/python-study/django/welcome_to_the_django_16' \

In: getcwd \
Out: `<built-in function getcwd>` \

In: xyz
Out: `<built-in function getcwd>` \

In: id(getcwd), id(xyz), id(os.getcwd) \
Out: (135731017946976, 135731017946976, 135731017946976) \

---

TODOs:
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

`import os` # NOTE¹ NOTE² NOTE³ NOTE⁴ NOTE⁵ NOTE⁶

`def main():` \

    print('Hello world!')
    print("This is Alice's greeting.")
    print('This is bob\'s greeting.')

    `foo(5, 10)`

    print('=' * 10)
    text = 'The current working directory is '
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

`if __name__ == '__main__':`

    main()
