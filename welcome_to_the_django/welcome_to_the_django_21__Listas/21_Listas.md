# AULA 21

INFO => O que é uma lista? Listas são sequencias mutáveis. A lista armazena uma referência para todos os obejtos dentro dela.

lista_de_frutas = ['Maçã', 'Banana', 'Uva', 'Laranja', 'Abacaxi']

In: lista_frutas = ['Maçã', 'Banana', 'Uva', 'Laranja', 'Abacaxi']

In: type(lista_frutas)
Out:
    list

In: lista_frutas
Out:
    ['Maçã', 'Banana', 'Uva', 'Laranja', 'Abacaxi']

In: lista_frutas.append('Marácuja') NOTE¹
In: lista_frutas
Out:
    ['Maçã', 'Banana', 'Uva', 'Laranja', 'Abacaxi', 'Marácuja']

In: lista_frutas.sort() NOTE²
In: lista_frutas
Out:
    ['Abacaxi', 'Banana', 'Laranja', 'Marácuja', 'Maçã', 'Uva']

In: lista_frutas.sort(reverse = True)
In: lista_frutas
Out:
    ['Uva', 'Maçã', 'Marácuja', 'Laranja', 'Banana', 'Abacaxi']

NOTE¹, NOTE² => O retorno do append e do sort é '*None*' isso, porque eles alteram a lista inicial.

---

## Uma lista pode armazenar qualquer tipo de objeto

lista_sortida = [1, 'Laura', False, 25.3, funcao_exemplo()]

In: def funcao_exemplo():
        pass

In: lista_sortida = [1, 'Laura', False, 25.3, funcao_exemplo]
In: lista_sortida
Out:
    [1, 'Laura', False, 25.3, <function __main__.funcao_exemplo()>]

In: lista_sortida = [1, 'Laura', False, 25.3, funcao_exemplo, funcao_exemplo()]
In: lista_sortida
Out:
    [1, 'Laura', False, 25.3, <function __main__.funcao_exemplo()>, None]

In: def funcao_retorna_1():
        return 1

In: lista_sortida = [1, 'Laura', False, 25.3, funcao_exemplo, funcao_exemplo(),len, [1, 2, 3], funcao_retorna_1()]
In: lista_sortida
Out:
    [1,
     'Laura',
     False,
     25.3,
     <function __main__.funcao_exemplo()>,
     None,
     <function len(obj, /)>,
     [1, 2, 3],
     1]

---

## É possível fazer uma copia da lista

Exemplo de função com cópia podendo alterar:

In: lista_sortida_1 = lista_sortida

In: lista_sortida, lista_sortida_1
Out:
    [1,
     'Laura',
     False,
     25.3,
     <function __main__.funcao_exemplo()>,
     None,
     <function len(obj, /)>,
     [1, 2, 3],
     1],
    [1,
     'Laura',
     False,
     25.3,
     <function __main__.funcao_exemplo()>,
     None,
     <function len(obj, /)>,
     [1, 2, 3],
     1]

In: lista_sortida.append(25/3)

In: lista_sortida
Out:
    [1,
     'Laura',
     False,
     25.3,
     <function __main__.funcao_exemplo()>,
     None,
     <function len(obj, /)>,
     [1, 2, 3],
     1,
     8.333333333333334]

In: lista_sortida_1
Out:
    [1,
     'Laura',
     False,
     25.3,
     <function __main__.funcao_exemplo()>,
     None,
     <function len(obj, /)>,
     [1, 2, 3],
     1,
     8.333333333333334]

In: def funcaoX(x):
        x.append(42)
        return x

In: funcaoX(lista_sortida), lista_sortida_1
Out:
    ([1,
      'Laura',
      False,
      25.3,
      <function __main__.funcao_exemplo()>,
      None,
      <function len(obj, /)>,
      [1, 2, 3],
      1,
      8.333333333333334,
      42],
     [1,
      'Laura',
      False,
      25.3,
      <function __main__.funcao_exemplo()>,
      None,
      <function len(obj, /)>,
      [1, 2, 3],
      1,
      8.333333333333334,
      42])

In: def funcaoY(y):
        y = y[:] => Isso não afetará a lista referencia
        y.append(51)
        return y

In: funcaoY(lista_sortida), lista_sortida_1
Out:
    ([1,
      'Laura',
      False,
      25.3,
      <function __main__.funcao_exemplo()>,
      None
      <function len(obj, /)>,
      [1, 2, 3],
      1,
      8.333333333333334,
      42,
      51],
     [1,
      'Laura',
      False,
      25.3,
      <function __main__.funcao_exemplo()>,
      None,
      <function len(obj, /)>,
      [1, 2, 3],
      1,
      8.333333333333334,
      42])

---

## Alterando lista dentro da lista

In: lista_com_lista_dentro = [1, 2, [4, 5, 6]]

In: lista_com_lista_dentro
Out:
    [1, 2, [4, 5, 6]]

In: lista_de_dentro = lista_com_lista_dentro[-1]

In: lista_de_dentro
Out:
    [4, 5, 6]

In: lista_de_dentro.append(77)

In: lista_de_dentro
Out:
    [4, 5, 6, 77]

In : lista_com_lista_dentro
Out:
    [1, 2, [4, 5, 6, 77]]
