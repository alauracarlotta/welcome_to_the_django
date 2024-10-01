# TOP 10 FUNÇÕES MAIS USADAS
# [Domine essas 10 Funções Obrigatórias em Python](https://www.youtube.com/watch?v=NB9pdUDNAJ4)
# 5 - FILTER

salarios = [1000, 5000, 7000, 850]

def filtrar_salarios(salario):
    salario_mais_alto = []
    if salario > 3000:
        salario_mais_alto.append(salario)
    return salario_mais_alto

# salarios_altos = list(filter(filtrar_salarios, salarios))
salarios_altos = list(filter(lambda x: x > 3000, salarios))
print(salarios_altos)