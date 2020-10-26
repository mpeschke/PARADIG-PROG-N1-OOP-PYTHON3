# coding=UTF-8
"""
Módulo: Representa a superclasse de um adversário na competição.
"""


class Adversario:
    """
    Superclasse representando um competidor nas olimpíadas.
    """
    _nome = None
    _resultado = None

    def __init__(self, nome, resultado):
        self._nome = nome
        self._resultado = resultado

    def nome(self):
        return self._nome

    def resultado(self):
        return self._resultado

