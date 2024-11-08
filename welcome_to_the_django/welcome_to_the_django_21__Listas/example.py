import os 


def main(): #NOTE ¹⁴ NOTE¹⁵ 
    print('Hello world!')
    print("This is Alice's greeting.")
    print('This is bob\'s greeting.')

    foo(5, 10)

    ###print('=' * 10)###
    text = 'The current working directory is '
    print(text + os.getcwd())

    foods = ['apples', 'oranges', 'bananas']

    for food in foods:
        print('I like to eat ', food)

    print('Count to ten: ')
    for i in range(1, 11):
        print(i)


def foo(a, b):
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

class Mamifero():
    def __init__(self, name, raca) -> None:
        self.name = name
        self.raca = raca
    
    def gato(self, cor, quatro_patas = True):
        self.cor = cor
        self.quatro_patas = quatro_patas
        if self.quatro_patas == False:
            print('Nosso amiguinho perneta')

if __name__ == '__main__': #
    main()
