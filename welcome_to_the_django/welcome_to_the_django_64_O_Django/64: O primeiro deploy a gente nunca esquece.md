# Aula 64

INFO =>  64: Pronto é quando está no ar!

PARA COLOCARMOS NOSSA APLICAÇÃO NO AR, USAREMOS O HEROKU!

Instalamos o heroku
Logamos com ele via terminal
    In: heroku login

O HEROKU NÃO É MAIS GRATUITO, SEGUI A AULA, MAS NÃO CONSEGUI COLOCAR A APP NO AR. SEGUINDO PARA OS PRÓXIMOS VÍDEOS.

AQUI ESTÁ SALVO O QUE EU FIZ NO TERMINAL CORRESPONDENTE A AULA 64. OS ARQUIVOS MEXIDOS E INCLUIDOS ESTÃO NA AULA 62.

4 2386
Not Found: /img/sponsor-silver-03.png
Not Found: /img/sponsor-silver-02.png
Not Found: /img/sponsor-silver-01.png
[05/Oct/2024 22:43:25] "GET /img/sponsor-silver-01.png HTTP/1.1" 404 2392
[05/Oct/2024 22:43:25] "GET /img/sponsor-silver-02.png HTTP/1.1" 404 2392
Not Found: /img/sponsor-gold-02.png
Not Found: /img/sponsor-silver-04.png
[05/Oct/2024 22:43:25] "GET /img/sponsor-silver-04.png HTTP/1.1" 404 2392
Not Found: /img/sponsor-gold-01.png
[05/Oct/2024 22:43:25] "GET /img/sponsor-gold-02.png HTTP/1.1" 404 2386
Not Found: /img/sponsor-silver-06.png
[05/Oct/2024 22:43:25] "GET /img/sponsor-silver-06.png HTTP/1.1" 404 2392
Not Found: /img/sponsor-silver-05.png
[05/Oct/2024 22:43:25] "GET /img/sponsor-silver-03.png HTTP/1.1" 404 2392
[05/Oct/2024 22:43:25] "GET /img/sponsor-silver-05.png HTTP/1.1" 404 2392
[05/Oct/2024 22:43:25] "GET /img/sponsor-gold-01.png HTTP/1.1" 404 2386

* History restored

laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62 (main)$ manage runserver
manage: comando não encontrado
laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62 (main)$ python manage.py runserver
Comando 'python' não encontrado, você quis dizer:
  comando 'python3' do deb python3
  comando 'python' do deb python-is-python3
laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62 (main)$ source .env/bin/activate
bash: .env/bin/activate: Arquivo ou diretório inexistente
laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62 (main)$ ll
total 32
drwxrwxr-x 4 laura-carlotta laura-carlotta 4096 out  5 18:53 ./
drwxrwxr-x 4 laura-carlotta laura-carlotta 4096 out  5 20:10 ../
-rw-rw-r-- 1 laura-carlotta laura-carlotta  387 out  5 18:48 asgi.py
drwxrwxr-x 6 laura-carlotta laura-carlotta 4096 out  5 19:26 core/
-rw-rw-r-- 1 laura-carlotta laura-carlotta    0 out  5 18:48 __init__.py
drwxrwxr-x 2 laura-carlotta laura-carlotta 4096 out  5 19:00 __pycache__/
-rw-rw-r-- 1 laura-carlotta laura-carlotta 3236 out  5 18:54 settings.py
-rw-rw-r-- 1 laura-carlotta laura-carlotta  852 out  5 18:57 urls.py
-rw-rw-r-- 1 laura-carlotta laura-carlotta  387 out  5 18:48 wsgi.py
laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62 (main)$ cd ..
laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ source .env/bin/activate
(.env) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
October 05, 2024 - 23:31:51
Django version 5.1.1, using settings 'dir62.settings'
Starting development server at [http://127.0.0.1:8000/]
Quit the server with CONTROL-C.

[05/Oct/2024 23:31:56] "GET / HTTP/1.1" 200 6132
^C(.env) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ git status
No ramo main
Your branch is up to date with 'origin/main'.

Arquivos não monitorados:
  (utilize "git add >>arquivo<<..." para incluir o que será submetido)
        ../../landingpage.zip
        ../welcome_to_the_django_40-desafios-pythonicos/
        ../welcome_to_the_django_41-desafios-pythonicos/
        ../welcome_to_the_django_42-desafios-pythonicos/
        ../welcome_to_the_django_43-desafios-pythonicos/
        ../welcome_to_the_django_44-desafios-pythonicos/
        ./

nada adicionado ao envio mas arquivos não registrados estão presentes (use "git add" to registrar)
(.env) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ cd ..
(.env) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django (main)$ git status
No ramo main
Your branch is up to date with 'origin/main'.

Arquivos não monitorados:
  (utilize "git add >>arquivo<<..." para incluir o que será submetido)
        ../landingpage.zip
        welcome_to_the_django_40-desafios-pythonicos/
        welcome_to_the_django_41-desafios-pythonicos/
        welcome_to_the_django_42-desafios-pythonicos/
        welcome_to_the_django_43-desafios-pythonicos/
        welcome_to_the_django_44-desafios-pythonicos/
        welcome_to_the_django_62_O_Django/

nada adicionado ao envio mas arquivos não registrados estão presentes (use "git add" to registrar)
(.env) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django (main)$ git add ../landingpage.zip
(.env) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django (main)$ git add welcome_to_the_django_62_O_Django/
(.env) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django (main)$ git commit -m "feat: construct a landing page"
[main 971b4e8] feat: construct a landing page
 79 files changed, 10332 insertions(+)
 create mode 100644 landingpage.zip
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/62_A_landing_page.md
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/__init__.py
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/asgi.py
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/__init__.py
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/admin.py
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/apps.py
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/migrations/__init__.py
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/models.py
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/css/basalstyle/.gitignore
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/css/basalstyle/README.md
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/css/basalstyle/images/abstrato.png
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/css/basalstyle/images/grid-15-30-95-1140.png
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/css/basalstyle/index.html
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/css/basalstyle/sass/_buttons.scss
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/css/basalstyle/sass/_custom.scss
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/css/basalstyle/sass/_forms.scss
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/css/basalstyle/sass/_functions.scss
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/css/basalstyle/sass/_grid.scss
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/css/basalstyle/sass/_header.scss
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/css/basalstyle/sass/_images.scss
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/css/basalstyle/sass/_nav.scss
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/css/basalstyle/sass/_typography.scss
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/css/basalstyle/sass/_variables.scss
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/css/basalstyle/sass/style.sass
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/css/basalstyle/style.min.css
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/css/font-awesome.min.css
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/css/main.css
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/FontAwesome.otf
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/SinkinSans-200XLight-webfont.eot
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/SinkinSans-200XLight-webfont.svg
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/SinkinSans-200XLight-webfont.ttf
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/SinkinSans-200XLight-webfont.woff
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/SinkinSans-300Light-webfont.eot
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/SinkinSans-300Light-webfont.svg
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/SinkinSans-300Light-webfont.ttf
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/SinkinSans-300Light-webfont.woff
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/SinkinSans-400Regular-webfont.eot
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/SinkinSans-400Regular-webfont.svg
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/SinkinSans-400Regular-webfont.ttf
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/SinkinSans-400Regular-webfont.woff
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/SinkinSans-600SemiBold-webfont.eot
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/SinkinSans-600SemiBold-webfont.svg
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/SinkinSans-600SemiBold-webfont.ttf
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/SinkinSans-600SemiBold-webfont.woff
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/SinkinSans-700Bold-webfont.eot
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/SinkinSans-700Bold-webfont.svg
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/SinkinSans-700Bold-webfont.ttf
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/SinkinSans-700Bold-webfont.woff
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/fontawesome-webfont.eot
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/fontawesome-webfont.svg
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/fontawesome-webfont.ttf
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/fonts/fontawesome-webfont.woff
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/img/favicon.ico
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/img/logo.png
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/img/register-bg.jpg
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/img/sponsor-gold-01.png
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/img/sponsor-gold-02.png
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/img/sponsor-gold-03.png
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/img/sponsor-silver-01.png
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/img/sponsor-silver-02.png
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/img/sponsor-silver-03.png
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/img/sponsor-silver-04.png
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/img/sponsor-silver-05.png
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/img/sponsor-silver-06.png
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/img/top-bg.jpg
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/js/jquery-1.11.0.min.js
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/js/jquery-1.11.0.min.map
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/js/jquery.stellar.min.js
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/js/main.js
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/js/retina-1.1.0.min.js
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/static/js/smooth-scroll.js
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/templates/index.html
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/tests.py
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/core/views.py
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/settings.py
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/urls.py
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/dir62/wsgi.py
 create mode 100755 welcome_to_the_django/welcome_to_the_django_62_O_Django/manage.py
(.env) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django (main)$ git push
Enumerating objects: 94, done.
Counting objects: 100% (94/94), done.
Delta compression using up to 4 threads
Compressing objects: 100% (89/89), done.
Writing objects: 100% (92/92), 2.82 MiB | 1.64 MiB/s, done.
Total 92 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), completed with 2 local objects.
To github.com:alauracarlotta/welcome_to_the_django.git
   3396c8f..971b4e8  main -> main
(.env) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django (main)$ pip install python-decouple
Collecting python-decouple
  Downloading python_decouple-3.8-py3-none-any.whl.metadata (14 kB)
Downloading python_decouple-3.8-py3-none-any.whl (9.9 kB)
Installing collected packages: python-decouple
Successfully installed python-decouple-3.8
(.env) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django (main)$ cd welcome_to_the_django_62_O_Django/
(.env) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ pip install python-decouple
Requirement already satisfied: python-decouple in ./.env/lib/python3.12/site-packages (3.8)
(.env) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ deactivate
laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ source .venv/bin/activate
(.env) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ pip install dj-database-url
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.
    
    See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.

[notice] A new release of pip is available: 24.1.2 -> 24.2
[notice] To update, run: python3 -m pip install --upgrade pip
(.env) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ python3 -m pip install --upgrade pip
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.
    
    See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.

[notice] A new release of pip is available: 24.1.2 -> 24.2
[notice] To update, run: python3 -m pip install --upgrade pip
(.env) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ ll
total 32
drwxrwxr-x  4 laura-carlotta laura-carlotta 4096 out  5 21:22 ./
drwxrwxr-x 64 laura-carlotta laura-carlotta 4096 out  5 21:13 ../
-rw-rw-r--  1 laura-carlotta laura-carlotta 5206 out  5 20:46 62_A_landing_page.md
-rw-r--r--  1 laura-carlotta laura-carlotta    0 out  5 18:48 db.sqlite3
drwxrwxr-x  4 laura-carlotta laura-carlotta 4096 out  5 18:53 dir62/
-rw-rw-r--  1 laura-carlotta laura-carlotta   88 out  5 21:27 .env
-rwxrwxr-x  1 laura-carlotta laura-carlotta  661 out  5 18:48 manage.py*
drwxrwxr-x  5 laura-carlotta laura-carlotta 4096 out  5 18:46 .venv/
(.env) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ deactivate
laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ python -m venv .venv
Comando 'python' não encontrado, você quis dizer:
  comando 'python3' do deb python3
  comando 'python' do deb python-is-python3
laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ python3 -m venv .venv
laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ source .venv/bin/activate
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ pip install dj-database-ur
ERROR: Could not find a version that satisfies the requirement dj-database-ur (from versions: none)
ERROR: No matching distribution found for dj-database-ur
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ pip install dj-database-url
Collecting dj-database-url
  Downloading dj_database_url-2.2.0-py3-none-any.whl.metadata (12 kB)
Collecting Django>=3.2 (from dj-database-url)
  Using cached Django-5.1.1-py3-none-any.whl.metadata (4.2 kB)
Collecting typing-extensions>=3.10.0.0 (from dj-database-url)
  Using cached typing_extensions-4.12.2-py3-none-any.whl.metadata (3.0 kB)
Collecting asgiref<4,>=3.8.1 (from Django>=3.2->dj-database-url)
  Using cached asgiref-3.8.1-py3-none-any.whl.metadata (9.3 kB)
Collecting sqlparse>=0.3.1 (from Django>=3.2->dj-database-url)
  Using cached sqlparse-0.5.1-py3-none-any.whl.metadata (3.9 kB)
Downloading dj_database_url-2.2.0-py3-none-any.whl (7.8 kB)
Using cached Django-5.1.1-py3-none-any.whl (8.2 MB)
Using cached typing_extensions-4.12.2-py3-none-any.whl (37 kB)
Using cached asgiref-3.8.1-py3-none-any.whl (23 kB)
Using cached sqlparse-0.5.1-py3-none-any.whl (44 kB)
Installing collected packages: typing-extensions, sqlparse, asgiref, Django, dj-database-url
Successfully installed Django-5.1.1 asgiref-3.8.1 dj-database-url-2.2.0 sqlparse-0.5.1 typing-extensions-4.12.2
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ pip install dj-static
Collecting dj-static
  Downloading dj-static-0.0.6.tar.gz (3.4 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting static3 (from dj-static)
  Downloading static3-0.7.0.tar.gz (24 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: dj-static, static3
  Building wheel for dj-static (pyproject.toml) ... done
  Created wheel for dj-static: filename=dj_static-0.0.6-py3-none-any.whl size=3054 sha256=e3422ff3f24fcb8a5037e83920bbb648092538cdd280f58d5eeca06986cc7dce
  Stored in directory: /home/laura-carlotta/.cache/pip/wheels/58/53/f9/d73c04cbf246490dadc83a1ab6de78f8abb7f49fc5f5aeea77
  Building wheel for static3 (pyproject.toml) ... done
  Created wheel for static3: filename=static3-0.7.0-py3-none-any.whl size=18597 sha256=d6b8f93aecf8b6c4460e8682e62bf1b65f24d2b9bfe487526ee8a8122c296e4f
  Stored in directory: /home/laura-carlotta/.cache/pip/wheels/cc/cc/10/99d7b1d6c50be9ee1c4bbed96e8726bb8d3a69186f25a57a6c
Successfully built dj-static static3
Installing collected packages: static3, dj-static
Successfully installed dj-static-0.0.6 static3-0.7.0
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ pip freeze
asgiref==3.8.1
dj-database-url==2.2.0
dj-static==0.0.6
Django==5.1.1
sqlparse==0.5.1
static3==0.7.0
typing_extensions==4.12.2
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ pip install python-decouple
Collecting python-decouple
  Using cached python_decouple-3.8-py3-none-any.whl.metadata (14 kB)
Using cached python_decouple-3.8-py3-none-any.whl (9.9 kB)
Installing collected packages: python-decouple
Successfully installed python-decouple-3.8
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ pip freeze
asgiref==3.8.1
dj-database-url==2.2.0
dj-static==0.0.6
Django==5.1.1
python-decouple==3.8
sqlparse==0.5.1
static3==0.7.0
typing_extensions==4.12.2
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ pip freeze > requirements.txt
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ cat requirements.txt
asgiref==3.8.1
dj-database-url==2.2.0
dj-static==0.0.6
Django==5.1.1
python-decouple==3.8
sqlparse==0.5.1
static3==0.7.0
typing_extensions==4.12.2
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django (main)$ git init
Repositório vazio Git inicializado em  /home/laura-carlotta/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django/.git/
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django$ ll
total 44
drwxrwxr-x  5 laura-carlotta laura-carlotta 4096 out  5 22:01 ./
drwxrwxr-x 64 laura-carlotta laura-carlotta 4096 out  5 21:13 ../
-rw-rw-r--  1 laura-carlotta laura-carlotta 5206 out  5 20:46 62_A_landing_page.md
-rw-r--r--  1 laura-carlotta laura-carlotta    0 out  5 18:48 db.sqlite3
drwxrwxr-x  4 laura-carlotta laura-carlotta 4096 out  5 18:53 dir62/
-rw-rw-r--  1 laura-carlotta laura-carlotta   88 out  5 21:27 .env
drwxrwxr-x  7 laura-carlotta laura-carlotta 4096 out  5 22:01 .git/
-rwxrwxr-x  1 laura-carlotta laura-carlotta  661 out  5 18:48 manage.py*
-rw-rw-r--  1 laura-carlotta laura-carlotta   39 out  5 22:00 Procfile
-rw-rw-r--  1 laura-carlotta laura-carlotta  187 out  5 21:57 requirements.txt
drwxrwxr-x  5 laura-carlotta laura-carlotta 4096 out  5 21:33 .venv/
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django$ ll -a
total 44
drwxrwxr-x  5 laura-carlotta laura-carlotta 4096 out  5 22:01 ./
drwxrwxr-x 64 laura-carlotta laura-carlotta 4096 out  5 21:13 ../
-rw-rw-r--  1 laura-carlotta laura-carlotta 5206 out  5 20:46 62_A_landing_page.md
-rw-r--r--  1 laura-carlotta laura-carlotta    0 out  5 18:48 db.sqlite3
drwxrwxr-x  4 laura-carlotta laura-carlotta 4096 out  5 18:53 dir62/
-rw-rw-r--  1 laura-carlotta laura-carlotta   88 out  5 21:27 .env
drwxrwxr-x  7 laura-carlotta laura-carlotta 4096 out  5 22:01 .git/
-rwxrwxr-x  1 laura-carlotta laura-carlotta  661 out  5 18:48 manage.py*
-rw-rw-r--  1 laura-carlotta laura-carlotta   39 out  5 22:00 Procfile
-rw-rw-r--  1 laura-carlotta laura-carlotta  187 out  5 21:57 requirements.txt
drwxrwxr-x  5 laura-carlotta laura-carlotta 4096 out  5 21:33 .venv/
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django$ git status
No ramo main

No commits yet

Arquivos não monitorados:
  (utilize "git add >>arquivo<<..." para incluir o que será submetido)
        .env
        .venv/
        62_A_landing_page.md
        Procfile
        db.sqlite3
        dir62/
        manage.py
        requirements.txt

nada adicionado ao envio mas arquivos não registrados estão presentes (use "git add" to registrar)
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django$ git status
No ramo main

No commits yet

Arquivos não monitorados:
  (utilize "git add >>arquivo<<..." para incluir o que será submetido)
        .gitignore
        62_A_landing_page.md
        Procfile
        dir62/
        manage.py
        requirements.txt

nada adicionado ao envio mas arquivos não registrados estão presentes (use "git add" to registrar)
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django$ git add .gitignore
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django$ git status
No ramo main

No commits yet

Mudanças a serem submetidas:
  (utilize "git rm --cached >>arquivo<<..." para não apresentar)
        new file:   .gitignore

Arquivos não monitorados:
  (utilize "git add >>arquivo<<..." para incluir o que será submetido)
        62_A_landing_page.md
        Procfile
        dir62/
        manage.py
        requirements.txt

(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django$ git commit -m "chore: add .gitignore"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email ["you@example.com"]
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'laura-carlotta@laura-carlotta-A315-53.(none)')
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django$ pwd
/home/laura-carlotta/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django$ git status
No ramo main

No commits yet

Mudanças a serem submetidas:
  (utilize "git rm --cached >>arquivo<<..." para não apresentar)
        new file:   .gitignore

Arquivos não monitorados:
  (utilize "git add >>arquivo<<..." para incluir o que será submetido)
        62_A_landing_page.md
        Procfile
        dir62/
        manage.py
        requirements.txt

(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django$ cd ../
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django (main)$ git status
No ramo main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (utilize "git add >>arquivo<<..." para atualizar o que será submetido)
  (use "git restore >>file<<..." to discard changes in working directory)
        modified:   ../.gitignore
        modified:   ../docs/dict.md
        modified:   welcome_to_the_django_62_O_Django/dir62/settings.py
        modified:   welcome_to_the_django_62_O_Django/dir62/wsgi.py

Arquivos não monitorados:
  (utilize "git add >>arquivo<<..." para incluir o que será submetido)
        welcome_to_the_django_40-desafios-pythonicos/
        welcome_to_the_django_41-desafios-pythonicos/
        welcome_to_the_django_42-desafios-pythonicos/
        welcome_to_the_django_43-desafios-pythonicos/
        welcome_to_the_django_44-desafios-pythonicos/
        welcome_to_the_django_62_O_Django/.gitignore
        welcome_to_the_django_62_O_Django/Procfile
        welcome_to_the_django_62_O_Django/requirements.txt
        welcome_to_the_django_63_O_Django/
        welcome_to_the_django_64_O_Django/

nenhuma modificação adicionada à submissão (utilize "git add" e/ou "git commit -a")
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django (main)$ git add welcome_to_the_django_62_O_Django/
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django (main)$ git status
No ramo main
Your branch is up to date with 'origin/main'.

Mudanças a serem submetidas:
  (use "git restore --staged >file<<..." to unstage)
        new file:   welcome_to_the_django_62_O_Django/Procfile
        modified:   welcome_to_the_django_62_O_Django/dir62/settings.py
        modified:   welcome_to_the_django_62_O_Django/dir62/wsgi.py
        new file:   welcome_to_the_django_62_O_Django/requirements.txt

Changes not staged for commit:
  (utilize "git add >>arquivo<<..." para atualizar o que será submetido)
  (use "git restore >file<<..." to discard changes in working directory)
        modified:   ../.gitignore
        modified:   ../docs/dict.md

Arquivos não monitorados:
  (utilize "git add >>arquivo<<..." para incluir o que será submetido)
        welcome_to_the_django_40-desafios-pythonicos/
        welcome_to_the_django_41-desafios-pythonicos/
        welcome_to_the_django_42-desafios-pythonicos/
        welcome_to_the_django_43-desafios-pythonicos/
        welcome_to_the_django_44-desafios-pythonicos/
        welcome_to_the_django_63_O_Django/
        welcome_to_the_django_64_O_Django/

(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django (main)$ git add ../.gitignore
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django (main)$ git add ../docs/
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django (main)$ git status
No ramo main
Your branch is up to date with 'origin/main'.

Mudanças a serem submetidas:
  (use "git restore --staged >file<<..." to unstage)
        modified:   ../.gitignore
        modified:   ../docs/dict.md
        new file:   welcome_to_the_django_62_O_Django/Procfile
        modified:   welcome_to_the_django_62_O_Django/dir62/settings.py
        modified:   welcome_to_the_django_62_O_Django/dir62/wsgi.py
        new file:   welcome_to_the_django_62_O_Django/requirements.txt

Arquivos não monitorados:
  (utilize "git add >>arquivo<<..." para incluir o que será submetido)
        welcome_to_the_django_40-desafios-pythonicos/
        welcome_to_the_django_41-desafios-pythonicos/
        welcome_to_the_django_42-desafios-pythonicos/
        welcome_to_the_django_43-desafios-pythonicos/
        welcome_to_the_django_44-desafios-pythonicos/
        welcome_to_the_django_63_O_Django/
        welcome_to_the_django_64_O_Django/

(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django (main)$ git add welcome_to_the_django_63
fatal: pathspec 'welcome_to_the_django_63' não encontrou nenhum arquivo
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django (main)$ git add welcome_to_the_django_63_O_Django/
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django (main)$ git add welcome_to_the_django_64_O_Django/
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django (main)$ git commit -m "import files"
[main e3e6e5a] import files
 8 files changed, 45 insertions(+), 12 deletions(-)
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/Procfile
 create mode 100644 welcome_to_the_django/welcome_to_the_django_62_O_Django/requirements.txt
 create mode 100644 welcome_to_the_django/welcome_to_the_django_63_O_Django/63_Pronto_e_quando_esta_no_ar.md
 create mode 100644 welcome_to_the_django/welcome_to_the_django_64_O_Django/64: O primeiro deploy a gente nunca esquece.md
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django (main)$ heroku apps:create welcometothedjango-laura
 ›   Warning: heroku update available from 7.60.1 to 9.3.0.
Creating ⬢ welcometothedjango-laura... !
 ▸    To create an app, verify your account by adding payment
 ▸    information. Verify now at https://heroku.com/verify Learn
 ▸    more at
 ▸    https://devcenter.heroku.com/articles/account-verification
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django (main)$ ll
total 260
drwxrwxr-x 64 laura-carlotta laura-carlotta 4096 out  5 21:13 ./
drwxrwxr-x 12 laura-carlotta laura-carlotta 4096 out  5 19:28 ../
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 set 10 19:18 pacote-desafios-pythonicos/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 31 22:50 welcome_to_the_django_01/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 23 16:43 welcome_to_the_django_02/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 23 16:52 welcome_to_the_django_03/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 23 16:54 welcome_to_the_django_04/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 23 17:10 welcome_to_the_django_05/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 23 16:57 welcome_to_the_django_06/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 23 17:29 welcome_to_the_django_07/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 23 17:43 welcome_to_the_django_08/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 23 18:31 welcome_to_the_django_09/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 23 18:57 welcome_to_the_django_10/
drwxrwxr-x  3 laura-carlotta laura-carlotta 4096 jul 24 19:35 welcome_to_the_django_14/
drwxrwxr-x  3 laura-carlotta laura-carlotta 4096 jul 24 21:53 welcome_to_the_django_15/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 24 22:47 welcome_to_the_django_16/
drwxrwxr-x  3 laura-carlotta laura-carlotta 4096 jul 25 14:23 welcome_to_the_django_17/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 25 17:04 welcome_to_the_django_18/
drwxrwxr-x  3 laura-carlotta laura-carlotta 4096 jul 25 17:54 welcome_to_the_django_19/
drwxrwxr-x  3 laura-carlotta laura-carlotta 4096 jul 28 18:48 welcome_to_the_django_20/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 31 23:21 welcome_to_the_django_21/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 31 23:20 welcome_to_the_django_22/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 ago  1 19:57 welcome_to_the_django_23/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 ago  1 20:30 welcome_to_the_django_24/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 ago 16 13:46 welcome_to_the_django_25/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 ago 16 13:50 welcome_to_the_django_26/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 ago 23 21:47 welcome_to_the_django_27/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 ago 23 22:52 welcome_to_the_django_28/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 ago 24 16:28 welcome_to_the_django_29/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 ago 24 20:25 welcome_to_the_django_30-desafios-pythonicos/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 ago 24 20:49 welcome_to_the_django_31-desafios-pythonicos/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 set  2 17:29 welcome_to_the_django_32-desafios-pythonicos/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 set  3 14:14 welcome_to_the_django_33-desafios-pythonicos/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 set  3 16:58 welcome_to_the_django_34-desafios-pythonicos/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 set  3 17:37 welcome_to_the_django_35-desafios-pythonicos/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 set  3 19:37 welcome_to_the_django_36-desafios-pythonicos/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 set  4 16:05 welcome_to_the_django_37-desafios-pythonicos/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 set  4 16:39 welcome_to_the_django_38-desafios-pythonicos/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 set  4 16:39 welcome_to_the_django_39-desafios-pythonicos/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 set  4 16:41 welcome_to_the_django_40-desafios-pythonicos/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 set 10 18:39 welcome_to_the_django_41-desafios-pythonicos/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 set 10 19:17 welcome_to_the_django_42-desafios-pythonicos/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 set 10 19:18 welcome_to_the_django_43-desafios-pythonicos/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 set 10 18:40 welcome_to_the_django_44-desafios-pythonicos/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 28 18:24 welcome_to_the_django_45-Expressoes-Regulares/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 28 18:24 welcome_to_the_django_46-Expressoes-Regulares/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 28 18:24 welcome_to_the_django_47-Expressoes-Regulares/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 28 18:24 welcome_to_the_django_48-Expressoes-Regulares/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 28 18:25 welcome_to_the_django_49-Expressoes-Regulares/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 28 18:25 welcome_to_the_django_50-Expressoes-Regulares/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 28 18:25 welcome_to_the_django_51-Expressoes-Regulares/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 28 18:34 welcome_to_the_django_52-Orientacao-a-Objeto/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 28 18:34 welcome_to_the_django_53-Orientacao-a-Objeto/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 28 18:34 welcome_to_the_django_54-Orientacao-a-Objeto/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 28 18:34 welcome_to_the_django_55-Orientacao-a-Objeto/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 28 18:35 welcome_to_the_django_56-Orientacao-a-Objeto/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 jul 28 18:35 welcome_to_the_django_57-Orientacao-a-Objeto/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 out  1 17:06 welcome_to_the_django_58_O_Django/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 out  1 17:34 welcome_to_the_django_59_O_Django/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 out  2 21:57 welcome_to_the_django_60_O_Django/
drwxrwxr-x  4 laura-carlotta laura-carlotta 4096 out  5 18:43 welcome_to_the_django_61_O_Django/
drwxrwxr-x  5 laura-carlotta laura-carlotta 4096 out  5 22:14 welcome_to_the_django_62_O_Django/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 out  5 20:50 welcome_to_the_django_63_O_Django/
drwxrwxr-x  2 laura-carlotta laura-carlotta 4096 out  5 21:14 welcome_to_the_django_64_O_Django/
-rw-rw-r--  1 laura-carlotta laura-carlotta  194 jul 23 19:06 welcome_to_the_django_OTHERS.md
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django (main)$ cd welcome_to_the_django_62_O_Django/
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django$ ll
total 44
drwxrwxr-x  5 laura-carlotta laura-carlotta 4096 out  5 22:14 ./
drwxrwxr-x 64 laura-carlotta laura-carlotta 4096 out  5 21:13 ../
-rw-rw-r--  1 laura-carlotta laura-carlotta 5206 out  5 20:46 62_A_landing_page.md
-rw-r--r--  1 laura-carlotta laura-carlotta    0 out  5 18:48 db.sqlite3
drwxrwxr-x  4 laura-carlotta laura-carlotta 4096 out  5 18:53 dir62/
-rw-rw-r--  1 laura-carlotta laura-carlotta   88 out  5 21:27 .env
drwxrwxr-x  7 laura-carlotta laura-carlotta 4096 out  5 22:13 .git/
-rwxrwxr-x  1 laura-carlotta laura-carlotta  661 out  5 18:48 manage.py*
-rw-rw-r--  1 laura-carlotta laura-carlotta   39 out  5 22:02 Procfile
-rw-rw-r--  1 laura-carlotta laura-carlotta  187 out  5 21:57 requirements.txt
drwxrwxr-x  5 laura-carlotta laura-carlotta 4096 out  5 21:33 .venv/
(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
October 06, 2024 - 01:21:03
Django version 5.1.1, using settings 'dir62.settings'
Starting development server at [http://127.0.0.1:8000/]
Quit the server with CONTROL-C.

[06/Oct/2024 01:21:08] "GET / HTTP/1.1" 200 6132
[06/Oct/2024 01:21:09] "GET /static/js/main.js HTTP/1.1" 200 1670
[06/Oct/2024 01:21:09] "GET /static/js/retina-1.1.0.min.js HTTP/1.1" 200 2993
[06/Oct/2024 01:21:09] "GET /static/img/register-bg.jpg HTTP/1.1" 200 62399
[06/Oct/2024 01:21:09] "GET /static/fonts/SinkinSans-300Light-webfont.woff HTTP/1.1" 200 24096
[06/Oct/2024 01:21:09] "GET /static/fonts/SinkinSans-600SemiBold-webfont.woff HTTP/1.1" 200 24348
[06/Oct/2024 01:21:09] "GET /static/fonts/fontawesome-webfont.woff?v=4.1.0 HTTP/1.1" 200 83760
[06/Oct/2024 01:21:09] "GET /static/img/favicon.ico HTTP/1.1" 200 99678
^C(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django$ cat .env
SECRET_KEY=django-insecure-&ghhvqm#xculjb_(rya1cr0yor2q9^1ee4tf8jb7tufj6ihj!%
DEBUG=True(.venv) laura-carlotta@laura-carlotta-A315-53:~/dev-projects/python-study/welcome_to_the_django/welcome_to_the_django/welcome_to_the_django_62_O_Django$
