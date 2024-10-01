# TOP 10 FUNÇÕES MAIS USADAS
# [Domine essas 10 Funções Obrigatórias em Python](https://www.youtube.com/watch?v=NB9pdUDNAJ4)
# 9 - ZIP

funcionarios = [
    'Laura',
    'Joana',
    'Bia',
    'Marcela'
]

salarios = [1000, 2500, 850, 1750]

print(list(zip(funcionarios, salarios)))
print(dict(zip(funcionarios, salarios))) # => Permite que eue transforeme a lista em dict 

for funcionario, salario in zip(funcionarios, salarios):
    print(f'Novo salário da {funcionario} é de R${salario * 1.1:.2f} reais')