# Aula 59

INFO =>  Conheça o Django: Django é um framework web de alto nível escrito em Python que possibilita rápido desenvolvimento e designe pragmático.

ATENÇÃO:
    `A PIOR COISA QUE VOCÊ PODE FAZER É COMEÇAR PELOS MODELS!`
    `DJANGO É O SEU BANCO DE DADOS NA WEB! #snq`

    >>>   TOP DOWN
    >>>       X
    >>>   BOTTOM UP

- NÃO PENSAR NO BANCO DE DADOS PRIMEIRO E SIM EM COMO A INTERNET FUNCIONA!!!

O QUE ISSO QUER DIZER:
    A internet é toda baseada em request / Response, certo? __CERTO__!!

Request => Recebemos uma mesagem do cliente.
Com base nessas informaçẽos temos que tomar várias decisões:

    => Ele é um usuário? 
    => Eles está com a sessão aberta? 
    => Ele tem permição de estar naquela página? 
    => Você irá retornar pra ele uma coisa de cache? 
    => Como você vai compor a resposta? (O response)
    => Você vai armazenar em cache a resposta que será enviada para ele? 
    => Aquela resposta vai usar recursos externos como banco de dados ou uma outra infraestrutura? 
    => A partir desse request você vai estourar outras mensagerns pra outros componentes do seu sistema? E assim acionar uma fila de processamento do seu sistema? Ou disparar um e-mail?

## O django sempre estará baseado em texto

<Sempre será um texto!>

Ex:
HTTP REQUEST =>
    $ curl -iv [http://welcometothedjango.com.br]

    GET / HTTP /1.1
    User-Agent: curl/7.19.7 (universal-apple-darwin10.0) libcurl/7.19.7
    Host: welcometothedjango.com.br
    Accept: */*

(VERBO + CAMINHO + PROTOCOLO + CABEÇALHO + CORPO)
[HTTP REQUEST](/assets/images/http_request.png)

HTTP RESPONSE =>
    $ curl -i [http://welcometothedjango.com.br]

    HTTP /1.1 200 OK
    Server: nginx/0.7.65
    Content-Type: text/html charset=utf-8
    Cache-Control: max-age=600

    `
    <html>
        <head>
            <title>Welcome To The Django | Aprendendo Python e Django na Prática!</title>
            <link rel="stylesheet" type="text/css" href="/static/css/screen.css" media="screen"/>
        </head>
        <body>
            <h1>Welcome To The Django</h1>
        </body>
    </html>
    `
[HTTP RESPONSE](/assets/images/http_response.png)

## O Django nada mais é do que um pacote python

Podemos startar um projeto em django com o comando:
  `django-admin startproject <myproject>`

Contudo ele é apenas:

    repo/
        manage.py
        myproject/
            __init__.py
            settings.py
            urls.py
            wsgi.py

manage.py
    => Conecta o django com o settings.py (para inicializar num contexto. Em que contexto? Do seu projeto)
    Cada projeto seu pode ter uma sequencia de comandos que o manage.py encontra naturalmente para você fazer diversas rotinas (Ex: Carregar dados para o banco, fazer um dump de dados* (docs/dict.md), limpar cache, etc.)

urls.py =>
    URL conf: módulo de rotas do seu site, caminho da sua url (Você consegue ver a view, qual parte do seu código vai ser executado.)

settings.py =>
    Se você puder utilize apenas 1 file desse em seu projeto. Existem formas de organizar o seu código para que haja apenas um, mesmo você tendo ambientes de desenvolvimento, homolog ou prod. (Vale a pena - 'palavras do H. Bastos')

TODO: (Pesquisar)
wsgi.py =>
    Quem implementa a inteface de aplicação web python, utiliza uma PEP (Python Enhancement Proposals)* (docs/dict.md)
    Esse file é o entrepoint (se fosse JAVA, esse seria o __main__)
    Ele que vai receber cada requisição e que enviara cada resposta

## O Django app

O Django app não é um componente do sistema!!!

O Django app é uma biblioteca python que tem um modulo chamado models.py, isso porque o django exige que você tenha um arquivo models.py para carregar a aplicação que é inicializado. O django faz uma avaliação da relação entre os seus modelos.

    repo/
        manage.py
        myproject/
            __init__.py
            settings.py
            urls.py
            wsgi.py
            >>> myapp/ <<<
                __init__.py
                models.py
                tests.py
                views.py

Todo app, precisa estar no 'INSTALLED_APPS' => myproject/settings.py
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        '>>> myproject.myapp, <<<
    ]

## O manage.py

manage.py runserver => (Inicializa um servidos de desenvolvimento)
    Inicializa o processo python, instancia/inicializa o django que consome o settings, levanta todas as suas aplicações, valida todos os modelos e fica esperando o wsgi informar se tem alguma requisição chegando e entra no fluxo de requisição:

        REQUEST HANDLER

        1. Request Middleware 
        2. URLs Resolve
        3. View Middleware
        4. View
        5. Template Response Middleware
        6. Response Middleware

    Toda vez que chega um texto da requisição, esse texto é parseado, processado, transformado num objeto python de alto nível pra você não ter que ficar cortando string ou coisa do gênero e inicia um processo para cada etapa: 

    1. => Executa o middleware que é uma função global da aplicação que no settings ficam todos registrados. Esse middleware é uma classe que implementa até quatro métodos específicos. 
        1 middleware pode ter:
            1 request middleware, 
            1 view middleware, 
            1 Template response e 
            1 response middleware.
    Eles são executados toda vez que uma requisição passa pelo Request Middleware.

    Qual a vantagem disso?
        o Código do seu projeto não precisa fazer coisas genéricas, como por exemplo:
            Carregar  a sessão do usuário; Identificar o usuário; (Perguntar no cookie, olhar na sessão, carregar e instanciar o usuário). Imagina se a cada requisição o sistema tivesse que fazer esse processo...
        
        Tudo o que você usar muitas vezes, é tranformado num middleware pra ter menos código no seu projeto. Essa é uma forma de horizontalizar as funcionalidades do sistema, porque todas as rquisições acabaram passando por aquilo ali.

=> WIP 13:51 vídeo
