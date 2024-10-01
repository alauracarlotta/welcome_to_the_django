# FUNÇÕES LAMBDA OU FUNÇÕES ANÔNIMAS:
#       => FUNÇÃO QUE VOCÊ NÃO PRESIDA DEFINI-LA OU NOMEÁ-LA (CONSTROI SEM O def)
#       => CONSTRÓI AO MESMO TEMPO QUE USA.

# Exemplo Luiz Otávio

lista = [
    ['PRODUTO1', 15],
    ['PRODUTO2', 18],
    ['PRODUTO3', 6],
    ['PRODUTO4', 1],
    ['PRODUTO5', 3],
    ['PRODUTO6', 50],
    ['PRODUTO7', 25]
]


def func(item):
    return item[1]

# lista.sort(key = func)
# lista.sort(key = func, reverse = True)
# lista.sort(key = lambda item: item[1])
# print(lista)

# --------------------------------------
# OUTRO EXEMPLO

print(sorted(lista, key = lambda x: x[1]))
print(lista)
