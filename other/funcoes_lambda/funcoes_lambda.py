# FUNÇÕES LAMBDA OU FUNÇÕES ANÔNIMAS:
#       => FUNÇÃO QUE VOCÊ NÃO PRESIDA DEFINI-LA OU NOMEÁ-LA (CONSTROI SEM O def)
#       => CONSTRÓI AO MESMO TEMPO QUE USA.

"""
    EX: Avaliar o preço de um serviço e saber quanto imposto será cobrado sobre o mesmo. (O imposto correspondente será de 30%)
"""

# função normal
def funcao_normal_calcular_imposto(valor):
    imposto = valor * 30/100

    return imposto

valor = 1000

print(funcao_normal_calcular_imposto(valor))

# -------------------------------------------------
# função lambda:

# lambda x = x é o que eu receberei de parâmetro
# : x * 30 é o que eu receberei como resultado
# calcular_imposto = lambda x: x * 30/100

""" valor = 1000
taxa = 30
calcular_imposto = lambda valor, taxa: valor * taxa/100

print(calcular_imposto(valor, taxa)) """


# -------------------------------------------------
# A VERDADEIRA VANTAGEM DA função lambda:
# Quando vbocê aplica uma função em outro método Python

"""
    EX: .map()
"""

precos = [1000, 2000, 500, 25, 800, 10]

# impostos1 = list(map(funcao_normal_calcular_imposto, precos))
# print(impostos1)

impostos1 = list(map(lambda x: x * 30/100, precos))
print(impostos1)
