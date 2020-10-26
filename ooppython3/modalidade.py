# coding=UTF-8
"""
Módulo: Fornece a superclasse com todos os métodos necessários para
implementar uma modalidade de competição de olimpíadas.
"""


class Modalidade:
    """
    Superclasse representando uma modalidade de competição das olimpíadas.
    """
    _adversarios = []
    _input = None
    _entrada = None

    def __init__(self, inp):
        self._input = inp

    def lerentrada(self):
        pass

    def validarentrada(self):
        pass

    def iniciar(self):
        pass

    def vencedor(self):
        pass
