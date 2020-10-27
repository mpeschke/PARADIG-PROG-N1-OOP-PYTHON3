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
        """
        Construtor
        @param nome: nome do adversário (auxilia a identificar o vencedor)
        @param resultado: lista dos resultados do adversário
        """
        self._nome = nome
        self._resultado = resultado

    def nome(self):
        """
        Nome
        @return: nome do adversário
        """
        return self._nome

    def resultado(self):
        """
        Resultados do adversário
        @return: Lista de resultados
        """
        return self._resultado
