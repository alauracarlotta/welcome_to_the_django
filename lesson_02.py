"""
IMPORT > proga.py / progb.py
¹ NOTE =>
    rodando esse programa no terminal, veremos que o nome de retorno da linha 6 não será proga.py e sim __main__
    proga.py é o entrepoint, ele é passado para o interpretador
"""

# proga.py
"""print('begin', __name__)

print('Define fa')
def fa():
    print('dentro fa')

print('chama fa')
fa()

print('end', __name__) # NOTE¹"""

#progb.py
print('begin', __name__)
import proga # NOTE quando importado o proga.py no progb.py, o interpretador executa todo o proga

print('Define fb')
def fb():
    print('dentro fb')
    proga.fa()

print('chama fb')
fb()

print('end', __name__) # NOTE¹

# WARNING => esse arquivo não irá rodas, somente explicação
