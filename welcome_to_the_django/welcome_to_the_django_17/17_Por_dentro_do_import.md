# AULA 17

INFO => Fim explicação de como funciona o import e o entry point do arquivo python.

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

`import os`

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

`if __name__ == '__main__':` \

    main()

---

## PROGA.PY

NOTE¹ => Como estamos dentro do modulo, não há um self ou this para eu autoreferenciar, com isso o python tem esses atributos (ex: __name__, __file__) built-in para dar infomações sobre o módulo.

o entrypoint é o "proga.py". o Python sobreescreve o nome 'proga.py' por __main__

---

NOTE² => fazendo essa configuração, conseguimos que o proga seja tanto o programa principal como uma biblioteca (teste para verificar se ele é entrepoint ou biblioteca)

---

NOTE³ => Quando importamos o proga no progb, assim que ele é importado, o interpretador para a execução do progb, executa todo o proga e em seguida retorna a execução do progb.

---

NOTE⁴ => A partir do momento em que condicionamos o arquivo com o __name__, obrigamos o código a executar a função, somente caso o entrypoint seja aquele cara. Caso contrario, ele segue a ordem de linha de excução. E com essa configuração o proga pode ser tanto o programa principal como uma biblioteca. (Verifica se ele é o entrypoit ou biblioteca)

---

def linha():
    print('-' * 10, '\n')

print('1 - Begin', __name__) # NOTE¹ NOTE²
linha()

print('2 - Define fa')
def definefa():
    print('3 - Dentro de fa')
linha()

if __name__ == '__main__': # NOTE⁴
    print('4 - Chama fa')
    definefa()
    linha()

print('5 - End', __name__)

---

## PROGB.PY

def linha():
    print('-' * 10, '\n')

print('1 - Begin', __name__)
import proga #NOTE³
linha()

print('2 - Define fB')
def definefB():
    print('3 - Dentro de fB')
    print('Chama proga')
    proga.definefa()
linha()

print('4 - Chama fB')
definefB()
linha()

print('5 - End', __name__)
