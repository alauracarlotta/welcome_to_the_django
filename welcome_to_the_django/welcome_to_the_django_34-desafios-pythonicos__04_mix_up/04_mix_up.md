# MIX UP

* ✅ TODO utilizando o método replace()
    => Adicionei na vez passada

* ✅ TODO utilizando o slice do python
    => Basicamente, foi adicionado em todas as tentativas

* ✅ TODO juntar as strings com concatenação ou método join()
    => Feitas das duas maneiras

* ✅ TODO fazer tudo numa só linha
    => Feito também com concatenação e o slice do python

* ✅ TODO validação tendo dois caracteres ou mais
    => Condicional adicionada.

## Exercícios que eu executei na primeira vez

__SOLUTION 1__
`def mix_up(a, b):`
    if len(a) <= 2 and len(b) <= 2:
        return f'{a} {b}'

    two_letters_a = a[:2]
    two_letters_b = b[:2]
    completed_letters_a = two_letters_a + b[2:]
    completed_letters_b = two_letters_b + a[2:]
    result =  f'{completed_letters_b} {completed_letters_a}'
    return result

***

__SOLUTION 2__
`def mix_up(a, b):`
    if (len(a) and len(b)) <= 2:
        return ' '. join([a, b])

    list_names = [b, a]
    for cont in range(len(list_names)):
        letter_0 = b
        letter_1 = a

        for cont in range(2):
            list_names[cont] = list_names[cont].replace(letter_0[0], letter_1[0])
            list_names[cont] = list_names[cont].replace(letter_0[1], letter_1[1])

            letter_0 = a
            letter_1 = b

    list_names.reverse()
    result = ' '.join(list_names)
    #breakpoint()
    return result
