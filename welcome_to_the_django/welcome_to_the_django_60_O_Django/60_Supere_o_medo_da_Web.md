# Aula 60

INFO =>  A complexidade do browser

Como isso tudo funciona?

## Perguntas básicas

[o browser](/assets/images/o_browser.png)

* O que é?
* Como chego lá?
* Como represento?
* Onde está?
* Como falo?
* É feito de que?

## URL (Uniform Resource Locator)

Quando você acessa um site, precisa saber uma URL (Uniform Resource Locator) para poder acessá-lo. A parte principal dessa URL é o domínio.
O domínio é um nome único que vai conseguir identificar o seu servidor ou as suas páginas. Para conseguir um domínio, você deve pagar pelo direito de usá-lo por um período mínimo de 1 ano.

Vejamos alguns exemplos de domínio:

* cursoemvideo.com
* faetec.rj.gov.br
* github.io
* universidadebrasil.edu.br

Analisando os endereços acima, temos domínios com várias terminações, como .com, .gov.br, .io, .edu.br. Essas terminações indicam tecnicamente que o site é de uma instituição comercial, governamental, educacional, ONGs, artistas, etc.

Além disso, alguns desses ainda indicam o país (.br). Esses são os TLD (Top Level Domain).
    > GTLD: São TLDs genéricos, sem indicação de país. Alguns dos domínios genéricos são .com, .net, .gov, .org, .io, .info, .online, .store, etc.

    > ccTLD: São TLDs com designação do país (coutry code). Alguns dos domínios desse tipo são .com.br, .edu.us, .co.fr, .jp, .es, etc.

## O DNS

[DNS](/assets/images/domain_name_service.png)

A primeira coisa é o DNS (Domain Name Serfvice)* docs/dict.md

    >>> Manda a info para uma controladora de operação dns que associa o nome de dominio (ex: welcometothedjango.com.br) com um IP* docs/dict.md que retorna a consulta para o navegador. (REQUEST)

    >>> Agora em posse do número de IP, o browser faz uma busca através da internet, encontra a máquina em que nosso site está hospedado e retorna a página que solicitamos. (RESPONSE)

## INTERNET PROTOCOL

[IP](/assets/images/internet_protocol.png)

    >>> Entre o Request e o Response, tem um caminho a ser percorrido:
    (processo da minha máquina ir até o servidor e voltar)

    A internet é uma REDE de REDES! É o protocolo IP que tem todos os processos e instruções de como é que você roteia todos os pacotes para chegar no lugar certo. Então, quando o navegador pede para se conectar com o servidor do welcometothedjango, ele bate em vários lugares, que vai roteando e encontrando um caminho viável até chegar no servidor.

## TRANSMISSION CONTROL PROTOCOL

[TCP](/assets/images/transmission_control_protocol.png)

    Depois que máquina já sabe como chegar no servidor, eles começam a copnversa para transmitir informação entre eles, utilizando o protocolo TCP (protocolo confiável porque garante a entrega do pacote)

    A conversa é mais ou menos assim;
        > O cliente manda um pacote SYN (syncronize) par ao servidor ("Quero sincronizar com você para falar com você!")
        > O servidor entende isso e manda para o cliente um pacote SYN-ACK (syncronization - acknoledged) (que seria: "Beleza, tô te ouvindo!"), 
        > O cliente, por sua vez, manda de volta um pacote ACK para o servidor ("Fechou! Então eu vou começar a falar!")
            Quando isso acontece, esse triple hand checked, (aperto de mão em três etapas), ai sim a conexão acontece!
        > Com a conexão estabelecida, o cliente envia o request para o servidor. O servidor processa o request recebido, vai no banco de dados, toma várias decisões e monta um response para um cliente.
        > O cliente então, vai pegar a resposta, processar ela e exibir as informações no navegador.
        > Em seguida, o navegador envia um pacote FIN (final, para finalizar a conexão).  O cliente percebe que o servidor quer finalizar, então o cliente envia ao servidor um pacote FIN-ACK. O servidor responde com ACK
        > e ASSIM A CONEXÃO ESTÁ FINALIZADA.

## O HTTP Request

[http request](/assets/images/http_request.png)

    O Hypertext Transfer Protocol envia e recebe TEXTOS. 
    Esse texto tem um formato especifico:
        curl -iv http://welcometothdjango.com.br/ => curl acesso o comando http://welcom...

        Protocolo => http://
        host => welcometothdjango.com.br
        / => path, caminho

        A requisição tem o seguinte formato:

        GET / HTTP /1.1
        User-Agent: curl/7.19.7 (universal-apple-darwin10.0) libcurl/7.19.7
        Host: welcometothedjango.com.br
        Accept: */*

            GET / HTTP/1.1 
                => MÉTODO GET (OUTROS COMO: POST, UPDATE, DELETE) / PROTOCOLO E SUA VERSÃO / (NO FINAL TEM '\n' oculto - quebra de linha)

            User-Agent: curl/7.19.7 (universal-apple-darwin10.0) libcurl/7.19.7
            Host: welcometothedjango.com.br
            Accept: */*
                => Cabeçalho (nome do cabeçalho: 'User-Agent' - esquema chave-valor)

            (
                SE FOSSE UM POST, APÓS O CABEÇALHO, PODERIAMOS CONSTRUIR UM 'CORPO DA REQUEST', CRIANDO UM POST ENVIADO AS INFORMAÇÕES COLHIDAS DO FORMULÁRIO
            )

## O HTTP Response

[http response](/assets/images/http_response.png)

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

        HTTP/1.1 200 OK
            => status line (PROTOCOLO E SUA VERSÃO / STATUS CODE / STATUS MESSAGE OU RESPONSE MESSAGE)
            => 
                100 = indica que a solicitação foi recebida.
                200 = indica sucesso da solicitação.
                301 = indica que uma página foi movida para outro endereço.
                302 = indica que uma página foi movida temporariamente.
                400 = indica que a solicitação está incorreta.
                403 = indica que o acesso é proibido.
                404 = indica que a página não foi encontrada.
                410 = indica que o recurso não está mais disponível.
                500 = indica um erro interno do servidor.

        Server: nginx/0.7.65
        Content-Type: text/html charset=utf-8
        Cache-Control: max-age=600
            => Cabeçalho (nome do cabeçalho: 'User-Agent' - esquema chave-valor)
        
        `
        <html>
            <head>
                <title>Welcome To The Django | Aprendendo Python e Django na Prática!</title>
                <link rel="stylesheet" type="text/css" href="/static/css/screen.css" media="screen" />
                <script type='text/javascript' src='/static/js/jquery.js' />
            </head>
            <body>
                <h1>Welcome To The Django</h1>
            </body>
        </html>
        `
            => CORPO DA RESPOSTA (FOI ENVIADO PELO SERVIDOR E COMPÕE O RESPONSE)
            => HTML, ÁRVORE DOM (Document Object Model) - ÁRVORE HIERARQUICA
                => No caso, se é encontrado 'href' ou 'src', o browser para a leitura e referencia o dominio + o path para encontrar o que está referenciado no html. Em seguida dá continuidade na leitura do HTML.
                => Depois que a árvora dom está contruida, passamos para a 'render tree', onde o browser combina o dom com o css e irá renderizar o html lido e gerado. Esse render tree calcula como as informações serão exibidas na tela.
