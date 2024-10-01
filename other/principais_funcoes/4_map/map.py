# TOP 10 FUNÇÕES MAIS USADAS
# [Domine essas 10 Funções Obrigatórias em Python](https://www.youtube.com/watch?v=NB9pdUDNAJ4)
# 4 - MAP

salarios = [1000, 5000, 7000, 850]

def aumentar_salarios(salario):
    if salario > 3000:
        # novo_salario = salario * 1.08
        novo_salario = salario * 18/100
    else:
        # novo_salario = salario * 1.1
        novo_salario = salario * 10/100
    return novo_salario

# novos_salarios = list(map(aumentar_salarios, salarios))
novos_salarios = list(map(lambda x: x * 10/100, salarios))
print(novos_salarios)
