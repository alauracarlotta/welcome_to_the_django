# TOP 10 FUNÇÕES MAIS USADAS
# [Domine essas 10 Funções Obrigatórias em Python](https://www.youtube.com/watch?v=NB9pdUDNAJ4)
# 3 - RANGE

lista = range(5)
print(lista)

lista0 = list(range(5))
print(lista0)

lista1 = list(range(1, 6))
print(lista1)

lista2 = list(range(1, 10, 2))
print(lista2)

lista3 = list(range(5, 0, -1))
print(lista3)

import time

for i in range(5, 0, -1):
    print(i, end='\r')
    time.sleep(1)

print('FIM!!')