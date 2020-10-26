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
        _module = importlib.import_module(modulo)
        _class = getattr(_module, classe)
        return _class(inp)
