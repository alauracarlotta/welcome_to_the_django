# FRONT BACK

TODO:

* ✅ Utilizar o slicing
    => Usei o fatiamento da string para separá-la em front e back

* ✅ Como calcular o índice?
    => Utilizei o módulo para calcular o índice da palavra

  * Pomemos utilizar:
    * ✅ Operadores aritiméticos;
    * ✅ Módulo;
    * TODO: Biblioteca math
      [rotina ceil](https://www.w3schools.com/python/trypython.asp?filename=demo_ref_math_ceil)

* Observações:
  * ✅Há repetição? O cálculo do índice está sendo feito separadamente, o seja, um cálculo para 'front' e outro para 'back'?
        => De certa forma, NÃO, pois utizo a separação por tamanho da palavra.

  * ✅ Há variáveis auxiliares tanto para o A quanto para o B?
        => Não, há listas que recebem seus valores conforme o fatiamento

  * TODO: encapsulamento (extrai a logica como comandos e reaplica ela)?
        => Voltar a esse exercício no futuro depois de POO
        [Encapsulamento-Youtube](https://www.youtube.com/watch?v=rw0uP9yNFCU)
        [Encapsulamento-Alura](https://cursos.alura.com.br/forum/topico-conceito-de-encapsulamento-104406)

  * ✅ Como está sendo concatenado as frentes com as partes de trás?
    Sugestão: operador + ou .join()
        => .join() pois sua usabilidade é melhor

## Exercícios que eu executei na primeira vez

__SOLUTION 1__
`def front_back(a, b):`
    # +++ SUA SOLUÇÃO +++
    index_a = len(a) // 2
    index_b = len(b) // 2

    if len(a) % 2 == 0:
        a_front = a[:index_a]
        a_back  = a[index_a:]
    else:
        a_front = a[:index_a + 1]
        a_back  = a[index_a + 1:]

    if len(b) % 2 == 0:
        b_front = b[:index_b]
        b_back  = b[index_b:]
    else:
        b_front = b[:index_b + 1]
        b_back  = b[index_b + 1:]
    result = f'{a_front}{b_front}{a_back}{b_back}'

    return result
