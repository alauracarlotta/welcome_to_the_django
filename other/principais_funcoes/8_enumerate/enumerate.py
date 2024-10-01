# TOP 10 FUNÇÕES MAIS USADAS
# [Domine essas 10 Funções Obrigatórias em Python](https://www.youtube.com/watch?v=NB9pdUDNAJ4)
# 8 - ENUMERATE

salarios = [1000, 5000, 7000, 850]

funcionarios = [
    'Laura',
    'Raul',
    'Walkyria',
    'Klaus'
]

for i, salario in enumerate(salarios):
    funcionario = funcionarios[i]
    print(f'Novo salário do(a) funcionário(a) {funcionario} é de R${salario + (salario * 10 / 100):.2f}!')
