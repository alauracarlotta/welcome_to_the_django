# Aula 61

INFO => Startando o projet

## VENV

A máquina Virtual docs/dict.md

In: python3 -m venv <nome_da_maquina_virtual> (ou)
In: python3 -m env .<nome_da_maquina_virtual>
<nome_da_maquina_virtual> => geralmente chamada de venv, env, .venv, .env

In: ls -a (Verifica todos os arquivos, incluindo os ocultos)
Out:
    .  ..  61.md  en../welcome_to_the_django_61_O_Django/61_Show_me_the_code.mdv

In: ls env
Out:
    bin  include  lib  lib64  pyvenv.cfg

In: ls env/bin
Out:
    activate  activate.csh  activate.fish  Activate.ps1  pip  pip3  pip3.12  python  python3  python3.12

In: source env/bin/activate
Out: (Levanta a virtual env, indicando )
    (env) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_61_O_Django (main)$

=> Vemos que estamos usando o python da virtual env agora
In: which python
Out:
    /home/laura-carlotta/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_61_O_Django/env/bin/python

## Agora podemos instalatr o django

In: pip install django

## E criar um novo projeto

In: django-admin startproject dir61 . (o . no final é bem importante, pois com isso não será criado um novo diretório)

In: ls
Out:
    61.md  dir61  env  manage.py

In: tree
Out:
    .
    |---- dir61
    |      |---- __init__.py (tranforma em um pacote python)
    |      |---- seetings.py
    |      |---- urls.py
    |      |---- wsgi.py
    |---- manage.py (entrypoit do django)

    1 directory, 5 files

In: python manage.py
Out:
    Type 'manage.py help >subcommand<' for help on a specific subcommand.

    Available subcommands:

    [auth]
        changepassword
        createsuperuser

    [contenttypes]
        remove_stale_contenttypes

    [django]
        check
        compilemessages
        createcachetable
        dbshell
        diffsettings
        dumpdata
        flush
        inspectdb
        loaddata
        makemessages
        makemigrations
        migrate
        optimizemigration
        sendtestemail
        shell
        showmigrations
        sqlflush
        sqlmigrate
        sqlsequencereset
        squashmigrations
        startapp
        startproject
        test
        testserver

    [sessions]
        clearsessions

    [staticfiles]
        collectstatic
        findstatic
        runserver

=> Para eu poder acessar o manage.py de qualquer diretório podemos fazer o seguinte:

In: cd dir61

In: echo VIRTUAL_ENV

In: echo VIRTUAL_ENV
Out:
    VIRTUAL_ENV

In: alias manage='python $VIRTUAL_ENV/../manage.py'

=> E pra ver que deu certo:

In: manage runserver
(Normalmente seria o comando `python manage.py runserver`)

## CRIANDO UMA APP

Uma app nada mais é do que uma biblioteca python que segue algumas convenções do django

In: python manage.py startapp core

(Por convenção, nomear o primeiro app de 'core' traz semântica ao projeto, pois isso significa o núcleo do projeto)

In: tree

Out:
    .                                                           => Dir trabalho
    |---- db.sqlite3                                            => banco de dados (banco de dev)
    |---- dir61                                                 => Dir Projeto
    |      |---- __init__.py (tranforma em um pacote python)
    |      |---- __pycache__                                    => Guarda as moficações *
    |      |      |---- __init__.cpython-312.pyc
    |      |      |---- settings.cpython-312.pyc
    |      |      |---- urls.cpython-312.pyc
    |      |      |---- wsgi.cpython-312.pyc
    |      |---- core                                           => Dir app
    |      |      |---- __init__.py
    |      |      |---- admin.py
    |      |      |---- apps.py
    |      |      |---- migrations
    |      |      |      |---- __init__.py
    |      |      |---- models.py
    |      |      |---- tests.py
    |      |      |---- views.py
    |      |---- seetings.py
    |      |---- urls.py
    |      |---- wsgi.py
    |---- manage.py (entrypoit do django)                      => manage

    4 directories, 17 files

* Dessa maneira, a próxima vez que eu executar meu programa (e eu NÃO mexer no file font.py) por ter o cache armazenado, o django eliminará uma série de processos e abrirá mais rápido o projeto.

> Dir de trabalho > Dir de projeto > Dir de app

### Instalar a app no settings do django

=> File settings.py

`INSTALLED_APPS = [`
    `'django.contrib.admin',`
    `'django.contrib.auth',`
    `'django.contrib.contenttypes',`
    `'django.contrib.sessions',`
    `'django.contrib.messages',`
    `'django.contrib.staticfiles',`
    `'dir61.core',`
`]`

=> File /core/apps.py

`from django.apps import AppConfig`

`class CoreConfig(AppConfig):`
    `default_auto_field = 'django.db.models.BigAutoField'`
    `name = 'dir61.core'`

### Criar a rota no url

(podemos usar caminhos/paths ou expressões regulares)

=> urls.py

`from django.contrib import admin`
`from django.urls import path`
`import dir61.core.views`

`urlpatterns = [`
    `path('', dir61.core.views.home),`
    `path('admin/', admin.site.urls),`
`]`

### Criando a views

`from django.shortcuts import render`

`def home(request):`
    `return render(request, 'index.html')`

=> Toda view do django é um objeto chamável, seja uma função, classe ou instancia. Ela sempre recebe como primeiro parâmetro uma instancia de HttpRequest e retorna necessáriamente uma instancia de HttpResponse.
Como primeiro parâmetro declaramos request, o espaço para receber essa instacia de HttpRequest. Usamos o shortcut 'render', que vai processar um request com o template que vamos criar, retornando uma instancia do HttpResponse.

=> Ou seja: 'O QUE É UMA VIEW DO DJANGO?'
    Ela é um objeto chamável que recebe um HttpRequest e retorna um HttpResponse

* Próxima etapa: Criar o template que queremos renderizar

### Criando o Template

=> Dir core

> Criamos o dir 'templates'
  > Criamos o file index.html

`<!DOCTYPE html>`
`<html lang="pt-br">`
`<head>`
    `<meta charset="UTF-8">`
    `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
    `<title>dir61</title>`
`</head>`
`<body>`
    `<h1>Welcome to the dir61!</h1>`
`</body>`
`</html>`

## RESUME

* Criamos uma Virtual Env
* Instalamos o django
* Criamos um projeto django, chamado 'dir61'
* Subimos o banco de dados
* Manejamos o arquivo 'manage.py' para que o manage consiga ser acessado de qualquer lugar
* Criamos uma app 'core'
* Instalamos a app core no settings
* Configuramos uma rota para a raiz do site
* Associamos essa rota a uma view 'home' dentro da app 'core'
* E essa view renderiza um arquivo index.html
