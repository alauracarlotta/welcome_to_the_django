# TOP 10 FUNÇÕES MAIS USADAS
# [Domine essas 10 Funções Obrigatórias em Python](https://www.youtube.com/watch?v=NB9pdUDNAJ4)
# 10 - OPEN

""" 
modos de leitura:
    a => append (acrescenta)
    r => read (lê)
    w => write (escreve)
"""


funcionarios = [
    'Laura',
    'Joana',
    'Bia',
    'Marcela'
]

salarios = [1000, 2500, 850, 1750]

# param = nome do file, modo de leitura, tipo de escrita
# arquivo = open('../welcome_to_the_django/other/principais_funcoes/10_open_with_open/fabrica.txt', 'w', encoding='utf-8')
arquivo = open('../welcome_to_the_django/other/principais_funcoes/10_open_with_open/fabrica.txt', 'a', encoding='utf-8')


for funcionario, salario in zip(funcionarios, salarios):
    if salario > 1500:
        salario = f'{(salario * 20 / 100):.2f}'
        arquivo.write(f'Novo salário da {funcionario} é de R${salario} reais (para mais de 1500)\n')
    else:
        salario = f'{(salario * 10 / 100):.2f}'
        arquivo.write(f'Novo salário da {funcionario} é de R${salario} reais (para pessoas comuns)\n')
# ATENÇÃO: Sempre se lembrar de fechar o arquivo.
arquivo.close()


""" arquivo = open('fabrica.txt', 'r', encoding='utf-8')
texto = arquivo.read()
print('Texto do arquivo: ')
print(texto)
# ATENÇÃO: Sempre se lembrar de fechar o arquivo.
arquivo.close() """


###################################
# RECOMENDADO: USAR COM A ESTRUTURA WITH
# Toda a estrutura é construida dentro do bloco do with. 
# Quando o bloco sair do with, o arquivo é automaticamente fechado.

with open('fabrica.txt', 'r', encoding='utf-8') as arquivo1:
    texto1 = arquivo1.read()
    print('Esse é outro texto DAQUI PARA FRENTEEEEEEEEEEEEEEEEEEEEEEEEEEE: ')
    print(texto1)
    
