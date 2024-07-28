nome = 'Henrique'

def indexes(var_nome):
    index_positive = ''
    index_negative = ''
    var_slice = ''
    for cont, value in enumerate(var_nome):
        index_positive += f'  {cont}'
        var_slice += f'  {value}'
        index_negative += f' -{len(var_nome)-cont}'
    
    print(index_positive)
    print(var_slice)
    print(index_negative)


if __name__ == '__main__':
    indexes(nome)