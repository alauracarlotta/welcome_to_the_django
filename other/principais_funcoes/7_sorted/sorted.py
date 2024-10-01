# TOP 10 FUNÇÕES MAIS USADAS
# [Domine essas 10 Funções Obrigatórias em Python](https://www.youtube.com/watch?v=NB9pdUDNAJ4)
# 7 - SORTED or sort

""" salarios = [1000, 5000, 7000, 850]

# salarios_ordenados = sorted(salarios)
salarios_ordenados = sorted(salarios, reverse = True)
print(salarios_ordenados) """

salarios = [
    (1000, 500, 80),
    (5000, 40, 200),
    (7000, 0, 0),
    (600, 4000, 150),
]

funcionarios = sorted(salarios, reverse = True, key = lambda x : sum(x))
print(funcionarios)

auxiliares = [('Laura',30, 185), ('Maria',25, 50), ('Joana',16, 82)]
auxiliares.sort(key=lambda x:x[2])
print(auxiliares)
