"""
IMPORT > proga.py / progb.py
¹ NOTE =>
    nota em lesson_02 file
"""

print('begin', __name__)

print('Define fa')
def fa():
    print('dentro fa')

# fazendo essa configuração, conseguimos que o proga seja tanto o programa principal como uma biblioteca (teste para verificar se ele é entrepoint ou biblioteca)
if __name__ == '__main__':
    print('chama fa')
    fa()

print('end', __name__)
