# lista mais rápida
# lista mais direta ao ponto

# CASO 1: DOBRAR O VALOR DO PRODUTO
def exemplo_normal(list):
    new_list = []
    for value in list:
        new_list.append(value * 2)
    return new_list

# Não preciso criar uma nova variável lista: O retorno já será uma nova lista
# 1º: Qual será o novo valor dessa lista? => value * 2
# 2º: => for value in list (Para cada item da minha lista)
def exemplo_list_comprehention(list):
    return [value * 2 for value in list]


def result(function):
    print(function)


lista_precos = [
    500,
    1500,
    2000,
    100,
    25
]

if __name__ == '__main__':
    result(exemplo_list_comprehention(lista_precos))