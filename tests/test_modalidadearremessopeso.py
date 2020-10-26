# coding=UTF-8
"""
Módulo: Testa a classe da modalidade de competição Arremesso de Peso das
olimpíadas.
"""
import unittest
from tests.utils import MockInput
from ooppython3.modalidadearremessopeso import ArremessoPeso, \
    NUMERO_ARREMESSOS


class TestModalidadeArremessoPeso(unittest.TestCase):
    """
    Classe representando a modalidade de competição Arremesso de Peso das
    olimpíadas.
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
        ap = ArremessoPeso(inp=inp)
        ap.lerentrada()
        self.assertEqual(ap._entrada,
                         '1.0,2.0,3.0',
                         "Esperada string '1.0,2.0,3.0'")

    def test_validar_entrada_valida(self):
        """
        Testa os parâmetros do construtor da classe.

        :return: None
        """
        inp = MockInput("1.0,2.0,3.0")
        ap = ArremessoPeso(inp=inp)
        ap.lerentrada()
        ret = ap.validarentrada()
        self.assertEqual(ret,
                         True,
                         "Função deveria ter retornado True")
        self.assertEqual(ap.arremessos,
                         [1.0, 2.0, 3.0],
                         "Esperada lista de floats [1.0, 2.0, 3.0]")
        self.assertEqual(len(ap.arremessos),
                         NUMERO_ARREMESSOS,
                         "Número de arremessos deveria ser {}".format(
                             NUMERO_ARREMESSOS)
                         )

    def test_validar_entrada_arremessos_a_menos(self):
        """
        Testa os parâmetros do construtor da classe.

        :return: None
        """
        inp = MockInput("1.0,2.0")
        ap = ArremessoPeso(inp=inp)
        ap.lerentrada()
        ret = ap.validarentrada()
        self.assertEqual(ret,
                         False,
                         "Função deveria ter retornado False")

    def test_validar_entrada_arremessos_a_mais(self):
        """
        Testa os parâmetros do construtor da classe.

        :return: None
        """
        inp = MockInput("1.0,2.0,3.0,4.0")
        ap = ArremessoPeso(inp=inp)
        ap.lerentrada()
        ret = ap.validarentrada()
        self.assertEqual(ret,
                         False,
                         "Função deveria ter retornado False")

    def test_validar_entrada_invalida(self):
        """
        Testa os parâmetros do construtor da classe.

        :return: None
        """
        inp = MockInput("1.0,invalido,3.0")
        ap = ArremessoPeso(inp=inp)
        ap.lerentrada()
        ret = ap.validarentrada()
        self.assertEqual(ret,
                         False,
                         "Função deveria ter retornado False")
