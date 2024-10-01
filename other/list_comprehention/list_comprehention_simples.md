# lista mais rápida
# lista mais direta ao ponto

# CASO 1: DOBRAR O VALOR DO PRODUTO
def exemplo_normal(list):
    new_list = []
    for value in list:
        new_list.append(value * 2)
    return print(new_list)

# Não preciso criar uma nova variável lista: O retorno já será uma nova lista
# 1º: Qual será o novo valor dessa lista? => value * 2
# 2º: => for value in list (Para cada item da minha lista)
def exemplo_list_comprehention(list):
    return print([value * 2 for value in list])


lista_precos = [
    501,
    1500,
    2013,
    100,
    25
]

if __name__ == '__main__':
    exemplo_list_comprehention(lista_precos)

In [2]: v = 'abc'

In [3]: v
Out[3]: 'abc'

In [4]: b = print(123)
123

In [5]: b

In [6]: b is None
Out[6]: True

In [7]: v is None
Out[7]: False

In [8]: t = 'Laura'

In [9]: v = 'Laura'

In [10]: t == v
Out[10]: True

In [11]: t is v
Out[11]: True

In [12]: v = 12345678912345678912345987

In [13]: v = 10500

In [14]: t = 10500

In [15]: v == t
Out[15]: True

In [16]: v is t
Out[16]: False

In [17]: n = 255

In [18]: m = 255

In [19]: n == m
Out[19]: True

In [20]: n is m
Out[20]: True

In [21]: n = 256

In [22]: m = 256

In [23]: n == m
Out[23]: True

In [24]: n is m
Out[24]: True

In [25]: n = 257

In [26]: m = 257

In [27]: n == m
Out[27]: True

In [28]: n is m
Out[28]: False

In [29]: id(n)
Out[29]: 126783748095056

In [30]: id(m)
Out[30]: 126783748090864

ponteiros = endereço de momemoria (apontar para o end de momria e não para a variavel propriamente dita)