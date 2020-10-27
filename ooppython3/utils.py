# coding=UTF-8
"""
Módulo: Fornece utilidades para o projeto.
"""
import importlib


class DynamicClassLoaderModalidade:
    """
    Instancia dinamicamente uma classe (objeto) a partir das informações
    de seu módulo e nome de classe.
    """
    @staticmethod
    def instancia(modulo, classe, inp):
        """
        Exemplo de construtor dinâmico de instâncias utilizando o importlib
        do Python. Utilizado aqui para instanciar dinamicamente as classes
        das modalidades de competição.
        @param modulo: módulo onde se encontra a classe a se instanciar.
        @param classe: nome da classe a instanciar.
        @param inp: instância da classe responsável pela entrada de dados.
        @return: instância da derivada da superclasse Modalidade
        (ArremessoPeso ou GinasticaOlimpica).
        """
        _module = importlib.import_module(modulo)
        _class = getattr(_module, classe)
        return _class(inp)
