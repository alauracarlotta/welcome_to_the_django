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

    2. => Em seguida o Django executa o URL resolve, que é parte integrante do projeto, que são as rotas, quais são as URLs do seu sistema (Essa URL mapeia para quais são as views)

    3. => Em sequencia, executa o view middleware (que é executado imediatamente antes da view ser chamada) porque no URL Resolve ele já pegou o caminho da requisição, comparou com a rota e descobriu qual é a view. Na sequecia, antes dela chamar a view, o Resolve executa o view middleware. O view middleare recebe exatamente quais são essas informações: Qual view será executada, quais são os parâmetros que serão executados, qual o request em questão.
    O request vai acumulando o estado do seu processo, nesse você inserir uma série de atributos adicionais, como se fosse um container de comunicação de cada etapa do processo django até gerar a resposta.
    Então se injeta as informações no request para quando cheagar na view, a resposta esteja disponível (por isso conseguimos fazer 'request.user', porque existe um request middleware da app de autenticação que consegue detectar que aquela request tem aquela informação de sessão que corresponde a um usuário e esse usuário está autorizado. Então carrega-se essa intancia do usuário no banco e injeta ela no request e quando chega na sua view, o request.user está disponível para ser usado naturalmente.)

    4. e 5. => Até chegar de fato na execução da view, essa é a sua lógica, esse é o pedaço de código de fato. A view retorna uma HTTP Response que passa para o template response, porque a resposta não necessáriamente é um texto ainda, ele é um objeto python e como é um objeto, podemos alterar o estado/texto/resposta dela

    6. => Passando então para a Response Middleware
        Ex de REQUAEST MIDDLEWARE e RESPONSE MIDDLEWARE:
            CACHE => O Cache quando é feito pela URL (tenho um blog, escrevi um artigo, esse artigo tem um título 'Raio X do Django', se 30 pessoas verem o artigo é o mesmo conteúdo. É um site que não precisa de login. Então para economizar e o django não ter que processar 30x a mesma coisa, eu faço um cache daquela página e com isso nem chega no django. Ele bate no Request Middleware que tem um middleware de cache e já retorna uma resposta direto do que está cacheado)
    
    Todo esse PIPELINE* docs/dict.md é um processo para você decidir onde você vai interferir no processamento do seu código para retornar a resposta o mais rápido possível

## O URL Resolve

    => O URL Conf : Módulo que que contém uma variável urlpatterns que referencia uma sequencia de rotas associadas às views.

        urlpatterns = [
            path('poll/', include('poll.urls')),
            path('admin/', admin.site.urls),
        ]

        Exemplo: Calcular tempo! ***LEMBRE: ALÉM DA ROTA, TEM UM VIEW PARA CADA UMA

            AO INVES DISSO:

                urlpatterns = patters( '',
                    url('^time/plus/1/$', one_hour_ahead),
                    url('^time/plus/2/$', two_hours_ahead),
                    ...
                    url('^time/plus/24/$', tons_hours_ahead),
                )

            FAÇA ISSO: (O urlpatters recebe como paramêtro uma expressão regular* docs/dict.md)

                urlpatterns = patters( '',
                    url('^time/plus/(\d{1,2})/$', time_ahead),
                )

                Será delegado para uma view que fará a conta retornará a lógica aplicada. Se estrutura uma view para que ela fique reutilizável em várias rotas
            
            ATENÇÃO:
                rota e view não é uma relação de 1 para 1. Pode ser de n para n
                Podemos ter n rotas para 1 view assim como n views para uma rota

    => URL Resolvers
        $ manage shell

            In: from django.core.urlresolvers import reverse, resolve

            In: resolve('/inscricao/1/')
            Out:
                (<function myproject.myapp.views.myview>, ('1',), {})
            
            In: reverse('myapp:detail', args=[1])
            Out:
                '/inscricao/1/'
        
        Resolve => Pega um path, um caminho da url e detecta qual é as view e os parâmetros que vão ser chamados.
        Reverse => É ao contrário: dada que eu tenho uma view e parâmetros ele consegue compor qual é a rota

        Isso é muito útil quando o cara do marketing quer trocar de 'inscrição' para 'cadastro'. Nesse caso, é só trocar no seu urls conf que nada quebra != se você tivesse chapado a url em string e aí teria que trocar em todo o que é lugar no código.
    
## Views

    View != Controller

    => Um callable* docs/dict.md que recebe uma instancia HTTP Request e retorna uma HTTP Response

    Uma pequena delegação/etapa do pipe que temos do Request Handler.

    Ex:
        from django.http impor HttpResponse

        def myview(request):
            return HttpResponse('Opa!')
    
    ===> ANTI-PATTERS
        * Views grandes; 

        * Conversões de dados na View;
            Ex: Request.post, converteu para string/decimal/inteiro está errado. A view só articula as outras partes do Django.

        * Pilhas de decoradores; 
        * Uso de funções auxiliares que instanciam o Http Response
        * Contextos de templates Gigantes

## FORMS

    => Muito além de 'formulários':
        Form:
            Responsável pelo pipeline de validação
            => Recebe-se um post com os dados de um formulário. A instancia da classe form vai processar/validar esses valores e te retornar tipos de auto nível. (Porque tudo o que vem pela rede é texto, porém o valor financeiro não é texto e quem converte isso são os 'fields' - valor que segue abaixo)

        Fields:
            Valida dados da requisição e os converte para tipos Python
            => [Vide form fields](/assets/images/form_fields.png)

        Widgets:
            representa o valor do field em HTML
            => [Vide form widgets](/assets/images/form_widgets.png)
    
    * ANATOMIA DE UM FORMFIELD
    [formField](/assets/images/anatomia_field.png)    
    O único lugar que tem conversão de texto é no field (vide imagem. Imagem mostra a conversão de valores inteiro. Ex: remove valores que o usuário coloca como .s e ,s e converte para texto)

- Exixtem 2 tipos de formulário:

    Bounded => USA PARA PROCESSAR
        (SubscriptionForm(request.Post), ou seja, com __dados__) (SOMENTE ESSA FORMA PODE SER VALIDADA)
        vs.
    Unbounded => USA APARA APRESENTAR
        (SubscriptionForm(), ou seja, SEM __dados__)

    >>> CICLO DE VALIDAÇÃO <<<

        * Dentro do form.isValid()
            1. Se form for bounded...
            2. Form full_clean()
            3. Para cada field é executado:
                3.1 clean() do Field
                3.2 validators do Field
                3.3 método clean_* se existir no forme
            4. Form clean()
            5. errors ou cleaned_data

## MODELS

    [models](/assets/images/models.png)

`from django.db import models`

`class Subscription(models.Model):`
    `name = models.CharField(max-length=100)`
    `cpf = models.CharField(max-length=11)`
    `email = models.EmailField()`
    `phone = models.CharField(max-length=20, blank=True)`
    `created_at = models.DateTimeField(auto_now_add=True)`

    `class Meta:`
        `ordering = ['created_at']`

    `def __unicode__(self):`
        `return self.name`
    
    => Ele 'reflete' como os dados acontecerão no SQL da tabela
    
    Conforme aquela descrição o django gera o esquema da tabela:

        CREATE TABLE "myapp_subscription" (
            "id" integer NOT NULL PRIMARY KEY,
            "name" varchar(100) NOT NULL,
            "cpf" varchar(11) NOT NULL UNIQUE,
            "email" varchar(75) NOT NULL UNIQUE,
            "phone" varchar(20) NOT NULL,
            "created_at" datetime NOT NULL
        );

### Modelo do ORM do Django

    1. In: type(Subscription)
    Out:
        <class 'django.db.models.base.ModelBase'>

    2. In: type(Subscription(...))
    Out:
        <class 'myproject.myapp.models.Subscription'>

    3. In: type(Subscription.objects)
    Out:
        <class 'django.db.models.manager.Manager'>

    4. In: type(Subscription.objects.all())
    Out:
        <class 'django.db.models.query.QuerySet'>

    1. >>> Subscription (TABELA)
    (Modelo)
    ... Descreve a estrutura de uma tabela

    2. >>> Subscription(...) (UMA LINHA DA TABELA)
    (A instancia do modelo reflete uma tupla)
    ... Corresponde a linha da tabela

    3. >>> Subscription.objects (TODAS AS LINHAS DA TABELA)
    (Manager do modelo é quem irá interagir com a tabela inteira, com todos os seus dados. Ele é que sabe fazer o 'select', é ele que conecta o ORM do Django que é o queryset - objeto python que acumula estados e que na hora que for necessário vai ser compilado para um query de acordo com o dribe de banco que está configurado no settings da aplicação. O queryset elimina gambiarras muito comuns como as feitas em PHP) 
    ... Manipula todas as linhas da tabela

    4. >>> Subscription.objects.all() (O ORM DO DJANGO)
    (Serve para todos os modelos - genérico (Toda vez que eu tenho uma coisa genérica interagindo com uma coisa específica, eu preciso de um intermediador, senão vira um RP (rp - tabela um 1 milhão de colunas para você configurar ele. ) O mediador é o manager (item 3). Esse é o cara que consegue dizer para um queryset (item 4) criar um queryset específico) ex: quero atualizar todos os usuários quie moram no Rio de Janeiro, essa operação não será feita num 'for', essa operação será feita no manager, porque ele faz um update daquela tabela com uma cláusula where) 
    ...Acumula estados que serão usados pelo ORM para compilar uma query SQL

### MODEL FIELDS

    => Correlacionam atributos do modelo com colunas da tabela (Não necessáriamente é uma relação de 1 para 1). Você poderá ter um campo que impactará duas colunas do banco de dados. Ex: Dinheiro - 2 campos: moeda e valor.

    In: $ manage shell

    In: from myproject.myapp.models import Subscription

    In: s = Subscription(
        name = "Henrique Bastos",
        cpf = "12345678901",
        email = "henrique@bastos.net",
        phone = "21-1234-4567"
    )

    In: s.save()

#### O QUE É POSSIVEL FAZER NO MODEL FIELDS

    => Conforme imagens, é mostrado tudo o que se pode fazer pelo django impactando no banco de dados:

[Subscription](/assets/images/Subscription.png)

[Insert or Update](/assets/images/insert_or_update.png)
Ele fará um insert ou update? Neste caso, fará um update pois já tem um id gerado.

[método get](/assets/images/metodo_get.png)
Para pegar um item especifico temos o método get (exceção: estoura um erro se não houver nenhuma ou mais de um.)

[filtros](/assets/images/filtros.png)
encadeamento = forma atributo__lookup (name__startswith="H")

[encademento](/assets/images/encadeamento.png)
Gera um queryset que permite fazer um encademento, acumulando o estado

[limit](/assets/images/limit.png)
Protocolo de slicing do python

[Update e delete](/assets/images/update_delete.png)
Pode-se fazer query in line

[meta](/assets/images/meta.png)
Todo modelo interno tem opcionalmente uma inner class Meta para configurar o modelo

## E finalmente caimos no TEMPLATES

Model / Form / Template => Principais caras de articulação que usamos na View. Na view teremos poucos detalhes do negócio, o que temos é muito mais uma 'orquestração' de como eles se relacionam, porque quando formos montar uma query complexa, não precisamos colocá-la na view, podemos implementar um método do manager, ao invés de converter um dado, usamos um form. Com isso conseguimos reduzir muito o tamanho da view delegando para os outros componentes do django a responsabvilidade para fazer esse trabalho de acordo com a sua especificidade. Então quanto mais alto nível trabalharmos com os campos de modelo, campos de formulário mais simples são as views, mais fácil é de testar o código e menos código é escrito para fazer coisas complexas.

[template variables](/assets/images/template_variables.png)

`<!DOCTYPE html>`
`<html lang="pt-br">`
`<head>`
    `<meta charset="UTF-8">`
    `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
    `<title>My Project</title>`
`</head>`
`<body>`
    `<img src="{{ STATIC_URL }}/img/logo.png">`
    `<h1>PARABÉNS, {{ subscription.name }}!</h1>`
    `<p>`
        `Sua inscrição foi realizada em`
        `{{ subscription.created_at | date:"d/m/Y" }}.`
    `</p>`
    `<p>`
        `Em breve, alguém entrará em contato pelo`
        `{% if subscription.phone %}`
            `telefone {{ subscription.phone }}.`
        `{% else %}`
            `email {{ subscription.email }}.`
        `{% endif %}`
    `</p>`
`</body>`
`</html>`

[variavel de contexto](/assets/images/variavel_contexto.png)
Acessa a variável de contexto que pode ser composto na view

[uso de templates](/assets/images/uso_templates.png)
Essa página poderá ser renderizada n vezes em n contextos diferentes.
