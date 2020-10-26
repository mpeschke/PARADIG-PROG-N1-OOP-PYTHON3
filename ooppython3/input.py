# coding=UTF-8
"""
Módulo: Fornece o mecanismo de entrada de input (stdin).
"""


class Input:
    """
    Encapsula o método 'input' do módulo 'sys'.
    Fundamental para habilitar mock para unit tests.
    """
    def input(self, mensagem):
        return input(mensagem)
