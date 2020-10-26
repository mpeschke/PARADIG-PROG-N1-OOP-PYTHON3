# coding=UTF-8
"""
Módulo: Testa a superclasse de um adversário na competição.
"""
import unittest
from ooppython3.adversario import Adversario


class TestAdversario(unittest.TestCase):
    """
    Superclasse representando um competidor nas olimpíadas.
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

    def test_construtor(self):
        """
        Testa os parâmetros do construtor da classe.

        :return: None
        """
        _nome = "meunome"
        _resultado = "meuresultado"
        ad = Adversario(nome=_nome, resultado=_resultado)
        self.assertEqual(ad.nome(),
                         _nome,
                         "Construtor incorreto para 'nome'")
        self.assertEqual(ad.resultado(),
                         _resultado,
                         "Construtor incorreto para 'resultado'")
