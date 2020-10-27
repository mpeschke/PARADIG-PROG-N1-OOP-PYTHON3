# coding=UTF-8
"""
Módulo: Testa a superclasse de uma modalidade de competição das olimpíadas.
"""
import unittest
from ooppython3.modalidade import Modalidade
from tests.utils import MockInput


class TestModalidade(unittest.TestCase):
    """
    Suíte de testes da superclasse representando uma modalidade de competição
    das olimpíadas.
    Notar o uso da classe MockInput para simular a entrada de dados
    sem o bloqueio do stadin real.
    """
    def test_inicializacao_superclasse(self):
        """
        Testa os parâmetros do construtor da classe.
        :return: None
        """
        inp = MockInput("1.0,2.0,3.0")
        ap = Modalidade(
            inp=inp,
            numtentativas=1000,
            numadversarios=500,
            mensagem="Can't touch this"
        )
        self.assertEqual(ap.adversarios(),
                         [],
                         "Esperada lista vazia [].")
        self.assertEqual(ap.numerotentativas(),
                         1000,
                         "Esperadas 1000 tentativas.")
        self.assertEqual(ap.numeroadversarios(),
                         500,
                         "Esperados 500 adversários.")
        self.assertEqual(ap._mensagem,
                         "Can't touch this",
                         "Esperada mensagem 'Can't touch this'.")
