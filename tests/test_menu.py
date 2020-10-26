# coding=UTF-8
"""
Módulo: Testa a classe de menu de escolha de modalidade de competição.
"""
import unittest
from ooppython3.menu import Menu, ID_MODALIDADE_ARREMESSOPESO, \
    ID_MODALIDADE_GINASTICAARTISTICA
from tests.utils import MockInput


class TestMenuModalidadeArremessoPeso(unittest.TestCase):
    """
    Testa a classe Menu.
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

    def test_lerentrada_modalidade_arremesso_peso(self):
        """
        Testa os parâmetros do construtor da classe.

        :return: None
        """
        _input = MockInput(ID_MODALIDADE_ARREMESSOPESO)
        menu = Menu(_input)
        menu.lerentrada()
        self.assertEqual(menu.validarmodalidade(),
                         True,
                         "Esperado resultado 'True'")

    def test_lerentrada_modalidade_ginastica_artistica(self):
        """
        Testa os parâmetros do construtor da classe.

        :return: None
        """
        _input = MockInput(ID_MODALIDADE_GINASTICAARTISTICA)
        menu = Menu(_input)
        menu.lerentrada()
        self.assertEqual(menu.validarmodalidade(),
                         True,
                         "Esperado resultado 'True'")

    def test_lerentrada_modalidade_inexistente_vazia(self):
        """
        Testa os parâmetros do construtor da classe.

        :return: None
        """
        _input = MockInput("")
        menu = Menu(_input)
        menu.lerentrada()
        self.assertEqual(menu.validarmodalidade(),
                         False,
                         "Esperado resultado 'False'")

    def test_lerentrada_modalidade_inexistente_espacos(self):
        """
        Testa os parâmetros do construtor da classe.

        :return: None
        """
        _input = MockInput("1 ")
        menu = Menu(_input)
        menu.lerentrada()
        self.assertEqual(menu.validarmodalidade(),
                         False,
                         "Esperado resultado 'False'")

    def test_lerentrada_modalidade_inexistente_texto_a_mais(self):
        """
        Testa os parâmetros do construtor da classe.

        :return: None
        """
        _input = MockInput("123deOliveira4")
        menu = Menu(_input)
        menu.lerentrada()
        self.assertEqual(menu.validarmodalidade(),
                         False,
                         "Esperado resultado 'False'")

    def test_menu_instancia_dinamica_arremesso_peso(self):
        """
        Testa os parâmetros do construtor da classe.

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
        Testa os parâmetros do construtor da classe.

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
