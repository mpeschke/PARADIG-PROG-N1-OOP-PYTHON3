# coding=UTF-8
"""
Módulo: Testa a classe de menu de escolha de modalidade de competição.
"""
import unittest
from ooppython3.menu import Menu, ID_MODALIDADE_ARREMESSOPESO, \
    ID_MODALIDADE_GINASTICAARTISTICA
from tests.utils import MockInput


class TestMenu(unittest.TestCase):
    """
    Suíte de testes para a classe Menu.
    Notar o uso da classe MockInput para simular a entrada de dados
    sem o bloqueio do stadin real.
    """
    def test_lerentrada_modalidade_arremesso_peso(self):
        """
        Testa cenário do caminho feliz (usuário digita modalidade existente).
        :return: None
        """
        menu = Menu(MockInput(ID_MODALIDADE_ARREMESSOPESO))
        menu.lerentrada()
        self.assertEqual(menu.validarmodalidade(),
                         True,
                         "Esperado resultado 'True'")

    def test_lerentrada_modalidade_ginastica_artistica(self):
        """
        Testa cenário do caminho feliz (usuário digita modalidade existente).
        :return: None
        """
        menu = Menu(MockInput(ID_MODALIDADE_GINASTICAARTISTICA))
        menu.lerentrada()
        self.assertEqual(menu.validarmodalidade(),
                         True,
                         "Esperado resultado 'True'")

    def test_lerentrada_modalidade_inexistente_vazia(self):
        """
        Testa cenário de erro de entrada (usuário digita modalidade
        inexistente).
        :return: None
        """
        menu = Menu(MockInput(""))
        menu.lerentrada()
        self.assertEqual(menu.validarmodalidade(),
                         False,
                         "Esperado resultado 'False'")

    def test_lerentrada_modalidade_inexistente_espacos(self):
        """
        Testa cenário de erro de entrada (usuário digita espaços).
        :return: None
        """
        menu = Menu(MockInput("1 "))
        menu.lerentrada()
        self.assertEqual(menu.validarmodalidade(),
                         False,
                         "Esperado resultado 'False'")

    def test_lerentrada_modalidade_inexistente_texto_a_mais(self):
        """
        Testa cenário de erro de entrada (usuário digita texto a mais).
        :return: None
        """
        menu = Menu(MockInput("123deOliveira4"))
        menu.lerentrada()
        self.assertEqual(menu.validarmodalidade(),
                         False,
                         "Esperado resultado 'False'")

    def test_menu_instancia_dinamica_arremesso_peso(self):
        """
        Testa cenário do caminho feliz (valida o retorno de uma instância
        da classe ArremessoPeso).
        :return: None
        """
        _input = MockInput(ID_MODALIDADE_ARREMESSOPESO)
        menu = Menu(_input)
        menu.lerentrada()
        menu.validarmodalidade()
        self.assertEqual(str(menu.modalidade(_input).__class__),
                         "<class 'ooppython3.modalidadearremessopeso.Arremess"
                         "oPeso'>",
                         "Esperada classe <class 'ooppython3.modalidadearreme"
                         "ssopeso.ArremessoPeso'>")

    def test_menu_instancia_dinamica_ginastica_artistica(self):
        """
        Testa cenário do caminho feliz (valida o retorno de uma instância
        da classe GinasticaArtistica).
        :return: None
        """
        _input = MockInput(ID_MODALIDADE_GINASTICAARTISTICA)
        menu = Menu(_input)
        menu.lerentrada()
        menu.validarmodalidade()
        self.assertEqual(str(menu.modalidade(_input).__class__),
                         "<class 'ooppython3.modalidadeginasticaartistica.Gin"
                         "asticaArtistica'>",
                         "Esperada classe <class 'ooppython3.modalidadeginast"
                         "icaartistica.GinasticaArtistica'>")
