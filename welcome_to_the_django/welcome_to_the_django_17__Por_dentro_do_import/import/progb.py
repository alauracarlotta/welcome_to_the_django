def linha():
    print('-' * 10, '\n')

print('1 - Begin', __name__)
import proga #NOTE¹²
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

print('5.6 - End', __name__)
