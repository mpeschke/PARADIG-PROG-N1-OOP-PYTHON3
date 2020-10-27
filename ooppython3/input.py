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
        """
        Coleta a entrada de dados do usuário, via stdin (bloqueia).
        @param mensagem: Mensagem de orientação para a entrada de dados.
        @return: dados entrados pelo usuário.
        """
        return input(mensagem)
