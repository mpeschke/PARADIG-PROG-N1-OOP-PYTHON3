# PARADIG-PROG-N1-OOP-PYTHON3 #

Tutorial em vídeo demonstrando a aplicação do paradigma OOP e detalhando as escolhas e implementações dessa aplicação:  

Atividade de entrega para a aula de Paradigmas de Linguagens de Programação (prof. Bruno Moritani).

Paradigmas: OOP (Object Oriented Programming - Programação Orientada a Objeto)  
Linguagem: Python 3 (3.6)  

## Local dependencies ##

You must install the following system dependencies:

Mac OS:  
>*\# source system-macos-dependencies.sh*  

Ubuntu 18:  
>*\# source system-ubuntu18-dependencies.sh*  

CentOS 7:  
>*\# source system-centos7-dependencies.sh*  

Execute os comandos:    

>*$ python3 -m venv .venv*  

>*$ source .venv/bin/activate*  

>*$ pip3 install -r requirements.txt*  

## Build ##

N/A

## Executando Testes Unitários ##

>*$ coverage run -m unittest discover*  

## Cobertura de Código ##

>*$ coverage report -m --omit=".venv/\*,tests/\*"*  

>*$ coverage html --omit=".venv/\*,tests/\*"*  

## Verificando a qualidade do código ##

>*$ pylint ooppython3/\*.py tests/\*.py*  