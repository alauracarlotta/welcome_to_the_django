# yield => cria um generator (torna o processo mais eficiente)
# generators


""" def ler_arquivo_csv(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.read()

if __name__ == '__main__':
    print(ler_arquivo_csv("other/yield/vendas.csv")) """

# ------------------------------------------

# ocupa um espaço pequeno em memoria
# "referencia o file mas não lê ele inteiro"

""" def ler_arquivo_csv(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.readlines()

lista = iter(ler_arquivo_csv("other/yield/vendas.csv"))
print(lista)

# iterator == generator

for item in lista:
    print(item) """
    
# --------------------------------------------

""" def ler_arquivo_csv(nome_arquivo):
    for linha in open(nome_arquivo, 'r'):
        yield linha

lista = ler_arquivo_csv("other/yield/vendas.csv")
print(lista)

print(next(lista))
print(next(lista))
print(next(lista))
print(list(lista)) """


# TESTING
# --------------------------------------------
""" import sys
for item in lista:
    print(item)
    print(type(lista))
    print(id(lista))
    print(sys.getsizeof(lista)) """

# ABREVIANDO
# --------------------------------------------

""" def ler_arquivo_csv(nome_arquivo):
    yield from open(nome_arquivo, 'r')

lista = ler_arquivo_csv("other/yield/vendas.csv")
print(lista)

for item in lista:
    print(item) """

# OUTRA AULA
# --------------------------------------------

def get_values():
    yield 'Laura'
    yield 'Laura123'
    yield 'Lauraaaaaaaaaaaaaaaaaa'

def example_get_values():
    for item in get_values():
        print(item)

example_get_values()

ver vídeo quando chegar na aula Orientação a Objeto (https://www.youtube.com/watch?v=tmeKsb2Fras)
