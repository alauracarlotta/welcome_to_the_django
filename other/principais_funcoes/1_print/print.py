# TOP 10 FUNÇÕES MAIS USADAS
# [Domine essas 10 Funções Obrigatórias em Python](https://www.youtube.com/watch?v=NB9pdUDNAJ4)
# 1 - PRINT

pessoa ={
    'nome': 'Laura',
    'idade': 30
}

print(f'A {pessoa["nome"]} tem {pessoa["idade"]} anos de idade.')

import time

print('contagem: ')
for i in range(5):
    # print(5 - i)
    # print(5 - i, end=' ')
    # print(5 - i, end='\n')
    print(5 - i, end='\r')
    # time.sleep(1)
print('Acabou!')

import pprint

aluna = {
    'nome': 'Laura',
    'idade': 30,
    'cidade': 'Jundiaí',
    'sexo_feminino': True,
    'sexo_feminino': True,
    'sexo_feminino': True
}
print('aluna', aluna)

teste = ['Laura', 30, 'Jundiaí', True, True, True]
teste.insert(0, teste[:])
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(teste)
