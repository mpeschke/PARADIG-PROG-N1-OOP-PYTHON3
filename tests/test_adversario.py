# coding=UTF-8
"""
Módulo: Testa a superclasse de um adversário na competição.
"""
import unittest
from ooppython3.adversario import Adversario


class TestAdversario(unittest.TestCase):
    """
    Suíte de testes para a superclasse de Adversário.
    """
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
