# AULA 14

INFO => (ipython ou jupyter notebook)
entendendo o interpretador e formas de adicionar stin e obter o stout de forma mais dinâmica ou com visual mais interativo.

- Linguagem:
  - Conj. de regras e gramáticas;

- Programa escrito em linguagem Python:
  - Ele terá um arquivo texto com a extensão .py;

- Interpretador:
  - Programa capaz de ler o código, interpretar e executar.

## iniciando python sem nenhum parâmetro, ele abrirá no modo interativo

In: `python3` \
Out: Python 3.12.3 (main, Apr 10 2024, 05:33:47) [GCC 13.2.0] on linux \
Type "help", "copyright", "credits" or "license" for more information. \
>>> .

In: `python3 -V` \
Out: Python 3.12.3 (24/07/2024)

In: `python3 -c print(40 + 2)` \
Out: 42

### Condutor STDIN (redirecionamento do linux)

INFO =>
  A Entrada Padrão (stdin) é a entrada de um fluxo de texto. Como exemplos temos o teclado, o mouse, um disquete, etc. Todos eles alimentam o computador com informações. Pode ser representado pelo número 0.

  A Saída Padrão (stdout) é a saída de um fluxo de texto em condições normais. Como exemplos temos o monitor, a impressora, o disquete, um arquivo, etc. Todos eles recebem informações do computador. Pode ser representado pelo número 1.

  A Saída de Erro (stderr) é a saída de um fluxo de texto em condições de erro ou insucesso em um determinado processamento. A saída de erro poderá ser direcionada para o monitor ou para um arquivo de LOG. Pode ser representado pelo número 2.

In: `echo "print(40 + 2)" | python -` \
Out: 42

In: vi meu_programa.py \

- In: print('python é', 40 + 2) \
  - In: python3 meu_programa.py
  - Out: python é 42 *ou*
  - In: python3 -i meu_programa.py
  - Out: python é 42
  >>> Com `python3 -i`, lerá o programa e depois abrirá o interpretador interativo.

### IPython ou Jupyter Notebook

Utilize o comando jupyter notebook no interpretador ao invés de ipython notebook. \
se você utilizar `ipython`, abrirá um interpretador com visual melhor.
