# coding=UTF-8
"""
Módulo: Testa a classe da modalidade de competição Ginástica Artística das
olimpíadas.
"""
import unittest
from tests.utils import MockInput
from ooppython3.modalidadeginasticaartistica import GinasticaArtistica, \
    NUMERO_NOTAS


class TestModalidadeArremessoPeso(unittest.TestCase):
    """
    Classe representando a modalidade de competição Ginástica Artística das
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
        inp = MockInput("1.0,2.0,3.0,4.0,5.0")
        ap = GinasticaArtistica(inp=inp)
        ap.lerentrada()
        self.assertEqual(ap._entrada,
                         '1.0,2.0,3.0,4.0,5.0',
                         "Esperada string '1.0,2.0,3.0,4.0,5.0'")

    def test_validar_entrada_valida(self):
        """
        Testa os parâmetros do construtor da classe.

        :return: None
        """
        inp = MockInput("1.0,2.0,3.0,4.0,5.0")
        ap = GinasticaArtistica(inp=inp)
        ap.lerentrada()
        ret = ap.validarentrada()
        self.assertEqual(ret,
                         True,
                         "Função deveria ter retornado True")
        self.assertEqual(ap.notas,
                         [1.0, 2.0, 3.0, 4.0, 5.0],
                         "Esperada lista de floats [1.0, 2.0, 3.0, 4.0, 5.0]")
        self.assertEqual(len(ap.notas),
                         NUMERO_NOTAS,
                         "Número de arremessos deveria ser {}".format(
                             NUMERO_NOTAS)
                         )

    def test_validar_entrada_arremessos_a_menos(self):
        """
        Testa os parâmetros do construtor da classe.

        :return: None
        """
        inp = MockInput("1.0,2.0")
        ap = GinasticaArtistica(inp=inp)
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
        inp = MockInput("1.0,2.0,3.0,4.0,5.0,6.0")
        ap = GinasticaArtistica(inp=inp)
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
        inp = MockInput("1.0,invalido,3.0,4.0,5.0")
        ap = GinasticaArtistica(inp=inp)
        ap.lerentrada()
        ret = ap.validarentrada()
        self.assertEqual(ret,
                         False,
                         "Função deveria ter retornado False")