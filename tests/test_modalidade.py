# coding=UTF-8
"""
Módulo: Testa a superclasse de uma modalidade de competição das olimpíadas.
"""
import unittest
from ooppython3.modalidade import Modalidade
from tests.utils import MockInput


class TestModalidade(unittest.TestCase):
    """
    Superclasse representando uma modalidade de competição das olimpíadas.
    """
    def setUp(self):
        """
        Inicializa data members da classe de suíte de testes.

        :return: None
        """
        pass

    def tearDown(self):
        """
        Destrói data members da classe de suíte de testes.

        :return: None
        """
        pass

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
