# TOP 10 FUNÇÕES MAIS USADAS
# [Domine essas 10 Funções Obrigatórias em Python](https://www.youtube.com/watch?v=NB9pdUDNAJ4)
# 2 - HELP

# help(print)

def calcular_imposto(faturamento, taxa):
    """
    Args:
        faturamento (float): O faturamento da empresa que vamos calcular o imposto
        taxa (float): A taxa percentual de imposto sobre o faturamento (ex: 0.2)

    Returns: imposto, faturamento_liquido
        imposto(float): Valor total do imposto calculado sobre o faturamento
        faturamento_liquido(float): Quanto sobrou do faturamento depois de descontado o imposto
    """
    imposto = faturamento * taxa
    return imposto, faturamento - imposto

print(calcular_imposto(1000, 12))
help(calcular_imposto)