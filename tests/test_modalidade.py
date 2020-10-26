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

    def test_ler_entrada(self):
        """
        Testa os parâmetros do construtor da classe.

        :return: None
        """
        inp = MockInput("1.0,2.0,3.0")
        ap = Modalidade(inp=inp)
        ap.lerentrada()
        self.assertEqual(ap._entrada,
                         None,
                         "Esperada variável não inicializada.")
