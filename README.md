Artur Jacques Nürnberg

Encurtador-de-URL
===

Esse programa tem como finalidade a criação de um página Web para criação de links encurtados.


Configurações da maquina que realizou a programação.

Python 3.7.4
Django 2.0.7


Ubuntu 
--------------------------------------------------------------------------------------

Primeiramente instale ubuntu 14.04.06 em uma maquina virtual (utilizei o Oracle VM virtual box)
Configuração da placa de rede em modo Bridge


Ubuntu 14.04.06
--------------------------------------------------------------------------------------
Anaconda

instalando Anaconda

$cd /tmp
$curl -O https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh

Verificando Data Integrity 

$sha256sum Anaconda3-2019.10-Linux-x86_64.sh

Instalando

$bash Anaconda3-2019.10-Linux-x86_64.sh

ativando conda

$source ~/.bashrc

Criando ambiente virtual

$conda create --name Django_env Python=3

Ativando ambiente

$conda activate Django_env


Instalando Django e realizando copia do repositório
--------------------------------------------------------------------------------------

$pip install Django

Instalando Git

$sudo apt install git-all

Clonando repositório

$cd home/user
$git clone https://github.com/arturjacques/Encurtador-de-URL

intalando bibliotecas

$pip install requests

migrando

$cd Encurtador-de-URL/
$python manage.py migrate

Inicializando (Em maquina virtual a rede deve estar em modo bridge)

$ifconfig

$python manage.py runserver <ip>:8000

(após constatado que o server está funcionando deve-se ir em trydjango/settings.py e alterar as
configurações de ALLOWED_HOSTS =['*'] para o IP da maquina)
