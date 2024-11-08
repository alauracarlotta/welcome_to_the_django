# Aula 67

INFO => Como manter as bibliotecas e o próprio Django atualizado?

>>> Compreenda o ciclo de releases do Django e como a comunidade atualiza o framework para que seus projetos nunca acumulem débito técnico mantendo-os sempre atualizados.

* Verificar no site do Django (ou o framework vigente) quais são as mudanças de uma realease para outra
[Django](https://www.djangoproject.com/)

[Realize de 07/11/2024](https://docs.djangoproject.com/en/5.1/releases/5.1.3/)

* Para atualizar o Django no seu projeto:
In: pip install --upgrade django
Out:
    Requirement already satisfied: django in ./.venv/lib/python3.12/site-packages (5.1.1)
  Collecting django
    Downloading Django-5.1.3-py3-none-any.whl.metadata (4.2 kB)
  Requirement already satisfied: asgiref<4,>=3.8.1 in ./.venv/lib/python3.12/site-packages (from django) (3.8.1)
  Requirement already satisfied: sqlparse>=0.3.1 in ./.venv/lib/python3.12/site-packages (from django) (0.5.1)
  Downloading Django-5.1.3-py3-none-any.whl (8.3 MB)
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.3/8.3 MB 15.1 MB/s eta 0:00:00
  Installing collected packages: django
    Attempting uninstall: django
      Found existing installation: Django 5.1.1
      Uninstalling Django-5.1.1:
        Successfully uninstalled Django-5.1.1
  Successfully installed django-5.1.3

* Com o In: `pip freeze` verificamos se foi tudo instalado como solicitamos:
Out:
  asgiref==3.8.1
  dj-database-url==2.2.0
  dj-static==0.0.6
  Django==5.1.3
  python-decouple==3.8
  sqlparse==0.5.1
  static3==0.7.0
  typing_extensions==4.12.2

NOTE
  >>> _Não esquecer de atualizar as novas versões no 'Requirements.txt' do projeto._

* Para verifica se algo quebrou de uma versão pra outra:
In: python manage.py check
Out:
  System check identified no issues (0 silenced).

* Sempre verificar o traceback *docs/dict.md

* Ultima coisa:
  * Verificar se os testes estão rodando:

  In: python manage.py test
  Out:
    Found 0 test(s).
    System check identified no issues (0 silenced).

    ----------------------------------------------------------------------
    Ran 0 tests in 0.000s

    NO TESTS RAN

  >>> _Como não possuimos testes nesta parte do projeto ainda, obtivemos o retorno acima_

* ATTENTION:
  Se você vizualisar a tag DEPRECATION WARNING no seu terminal, isso significa que aquela funcionalidade será removida numa realise a frente, isso serve para que você começe a se preparar para se adequar a essa determinada função no projeto.
