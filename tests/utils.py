# coding=UTF-8
"""
Módulo: Testa a classe de menu de escolha de modalidade de competição.
"""


class MockInput:
    """
    Mock para simular o método 'input' do módulo 'sys' sem bloquear a execução
    esperando pela entrada do usuário.
    """
    _retorno = None

    def __init__(self, retorno):
        self._retorno = retorno

    def input(self, mensagem):
        return self._retorno
