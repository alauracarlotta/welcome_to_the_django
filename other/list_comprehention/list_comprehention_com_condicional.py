# lista mais rápida
# lista mais direta ao ponto

# is serve para comparar endereço de memória

# CASO 2: SENDO O VALOR ACIMA DE 1000, CALCULE 50% A MAIS DO SEU VALOR
def exemplo_normal_somente_com_if(list):
    new_list = []
    for value in list:
        if value >=1000:
            # new_list.append(value + (value * 50/100))
            new_list.append(value + (value * 0.5))

    return new_list

# somente com if
def exemplo_list_comprehention_somente_com_if(list):
    return [value + (value * 50/100) for value in list if value > 1000]



def exemplo_normal_com_if_else(list):
    new_list = []
    for value in list:
        if value >=1000:
            # new_list.append(value + (value * 50/100))
            new_list.append(value + (value * 0.5))
        else:
            new_list.append(value + (value * 0.25))

    return new_list

# com if-else
def exemplo_list_comprehention_com_if_else(list):
    return [value + (value * 50/100) if value > 1000 else value + (value * 0.25) for value in list ]


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
    result(exemplo_list_comprehention_com_if_else(lista_precos))