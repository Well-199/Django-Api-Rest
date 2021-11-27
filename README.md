START/STOP -> 12. Instalação e configuração 20:00
--------------------------------------------------

mkdir nome_da_pasta

python -m venv venv

.\env\scripts\activate.bat

pip install django

django-admin startproject config -- usar config como padrao

cd nome_do_projeto

python manage.py runserver

python manage.py startapp nome_da_aplicação

deactivate
--------------------------------------------------

install mysql
pip install mysqlclient
---------------------------------------------------
Config DataBase
---------------------------------------------------
'ENGINE': 'django.db.backends.mysql',
'NAME': 'escola',
'HOST': 'localhost',
'USER': 'root',
'PASSWORD': '',
'PORT': '3306'
-----------------------------------------------------
Create table/ migrate
-----------------------------------------------------
python manage.py makemigrations
python manage.py migrate
