def linha():
    print('-' * 10, '\n')

print('1 - Begin', __name__) # NOTE¹⁰ NOTE¹¹
linha()

print('2 - Define fa')
def definefa():
    print('3 - Dentro de fa')
linha()

if __name__ == '__main__': # NOTE¹³
    print('4 - Chama fa')
    definefa()
    linha()

print('5 - End', __name__)
