# coding=UTF-8
"""
Módulo: Testa a classe de um adversário na modalidade Arremesso de Peso.
"""
import unittest
from ooppython3.adversarioarremessopeso import AdversarioArremessoPeso


class TestAdversarioArremessoPeso(unittest.TestCase):
    """
    Testes para a classe de um adversário na modalidade Arremesso de Peso.
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
        ad = AdversarioArremessoPeso(nome=_nome, resultado=_resultado)
        self.assertEqual(ad.nome(),
                         _nome,
                         "Construtor incorreto para 'nome'")
        self.assertEqual(ad.resultado(),
                         _resultado,
                         "Construtor incorreto para 'resultado'")
