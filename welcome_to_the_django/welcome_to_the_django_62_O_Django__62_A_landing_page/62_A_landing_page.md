# Aula 62

INFO => Landing page

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

## INICIANDO A LANDING PAGE

=> Baixamos os arquivos da 'landing page'
=> Dentro de core, criamos o dir 'static' e movemos para dentro dele: fonts, css, js e img
=> Substituimos a index que tinhamos criado, trocando pela que o nosso "designer" nos enviou.
=> Rodando a página, veremos que o servidor não encontrou basicamente todos os nossos arquivos staticos.

In: python manage.py runserver
Out:
    [05/Oct/2024 23:09:55] "GET / HTTP/1.1" 200 5996 <!-- Status 200 - encontrou a página -->
    Not Found: /css/font-awesome.min.css <!-- Todos os outros os quais não encontraram o arquivos, estarão com status 400 ou 404 -->
    Not Found: /css/main.css
    [05/Oct/2024 23:09:55] "GET /css/main.css HTTP/1.1" 404 2353
    Not Found: /js/jquery-1.11.0.min.js
    [05/Oct/2024 23:09:55] "GET /js/jquery-1.11.0.min.js HTTP/1.1" 404 2386
    [05/Oct/2024 23:09:55] "GET /css/font-awesome.min.css HTTP/1.1" 404 2389
    Not Found: /css/basalstyle/style.min.css
    Not Found: /js/retina-1.1.0.min.js
    [05/Oct/2024 23:09:55] "GET /css/basalstyle/style.min.css HTTP/1.1" 404 2401
    Not Found: /js/jquery.stellar.min.js
    [05/Oct/2024 23:09:55] "GET /js/retina-1.1.0.min.js HTTP/1.1" 404 2383
    Not Found: /js/main.js
    [05/Oct/2024 23:09:55] "GET /js/jquery.stellar.min.js HTTP/1.1" 404 2389
    Not Found: /css/font-awesome.min.css
    Not Found: /css/main.css
    [05/Oct/2024 23:09:55] "GET /css/main.css HTTP/1.1" 404 2353
    Not Found: /js/smooth-scroll.js
    [05/Oct/2024 23:09:55] "GET /js/main.js HTTP/1.1" 404 2347
    [05/Oct/2024 23:09:55] "GET /js/smooth-scroll.js HTTP/1.1" 404 2374
    [05/Oct/2024 23:09:55] "GET /css/font-awesome.min.css HTTP/1.1" 404 2389
    Not Found: /img/sponsor-silver-01.png
    Not Found: /img/sponsor-silver-04.png
    [05/Oct/2024 23:09:55] "GET /img/sponsor-silver-04.png HTTP/1.1" 404 2392
    Not Found: /img/sponsor-silver-02.png
    Not Found: /img/sponsor-gold-01.png
    [05/Oct/2024 23:09:55] "GET /img/sponsor-gold-01.png HTTP/1.1" 404 2386
    [05/Oct/2024 23:09:55] "GET /img/sponsor-silver-01.png HTTP/1.1" 404 2392
    [05/Oct/2024 23:09:55] "GET /img/sponsor-silver-02.png HTTP/1.1" 404 2392
    Not Found: /img/sponsor-silver-06.png
    [05/Oct/2024 23:09:55] "GET /img/sponsor-silver-06.png HTTP/1.1" 404 2392
    Not Found: /img/sponsor-silver-03.png
    Not Found: /img/sponsor-gold-02.png
    Not Found: /img/sponsor-silver-05.png
    [05/Oct/2024 23:09:55] "GET /img/sponsor-silver-05.png HTTP/1.1" 404 2392
    [05/Oct/2024 23:09:55] "GET /img/sponsor-gold-02.png HTTP/1.1" 404 2386
    [05/Oct/2024 23:09:55] "GET /img/sponsor-silver-03.png HTTP/1.1" 404 2392
    Not Found: /img/sponsor-gold-03.png

=> Os __status__ 400 ou 404, não fora encontrados pois o arquivo precisa referenciar com as ferramentas django.

=> Na primeira linha, antes da tag <<!DOCTYPE html>, temos que carregar o dir 'static' para que seja encontrado os outros diretórios. Assim como em seus respctivas refrenciações, os arquivos dever ser chamados no formato django. (Vide exemplo favicon, assim como css e js para os casos href e src)

{% load static %}
`<!DOCTYPE html>`
`<html lang="pt-br">`
`<head>`
    `<meta charset="UTF-8">`
    `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
    <!-- Favicon -->
    `<link rel="shortcut icon" href="{% static 'img/favicon.ico' %}">`
    <!-- CSS -->
    `<link rel="stylesheet" href="{% static 'css/font-awesome.min.css' %}">`
    `<link rel="stylesheet" href="{% static 'css/basalstyle/style.min.css' %}">`
    `<link rel="stylesheet" href="{% static 'css/main.css' %}">`
    <!-- js -->
    `<script src="{% static 'js/jquery-1.11.0.min.js' %}"></script>`
    `<script src="{% static 'js/jquery.stellar.min.js' %}"></script>`
    `<script src="{% static 'js/smooth-scroll.js' %}"></script>`
    `<script src="{% static 'js/retina-1.1.0.min.js' %}"></script>`
    `<script src="{% static 'js/main.js' %}"></script>`
    `<title>dir61</title>`
`</head>`
`<body>`
    `<h1>Welcome to the dir61!</h1>`
`</body>`
`</html>`

Para não ser necessários trocar todos os arquivos staticos linha a linha, usamos no vscode (ou no pycharm) a função replace, onde ele aceita um regex como parâmetro:

(Com as caixas 'match case' e regular expression (ou regx) habilitadas)
    Inserimos o regex na primeira caixa: (src|href)="((img|js|css).*?)"

Na segunda, inserimos a substituição:
    $1="{% static '$2' %}"

### A CONSTRUÇÃO DO REGEX

Precisamos pegar todos os arquivos href e src dos dirs img, css e js.
    FIND:
        A composição
            href="(.*)"
            (src|href)="(.*)"
            (src|href)="(.*?)"
            (src|href)="((img|css|js).*?)"

    REPLACE:
        $1="{% static '$2' %}"
