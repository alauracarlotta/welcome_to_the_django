# TOP 10 FUNÇÕES MAIS USADAS
# [Domine essas 10 Funções Obrigatórias em Python](https://www.youtube.com/watch?v=NB9pdUDNAJ4)
# 6 - SUM

custos_variados = [1000, 5000, 7000, 850]

""" def somar_custos(*custo):
    return sum(*custo)
print(somar_custos(custos))
"""

total_custos = sum(custos_variados, start=1200)
print(total_custos)