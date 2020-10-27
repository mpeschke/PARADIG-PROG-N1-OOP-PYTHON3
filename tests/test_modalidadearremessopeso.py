# coding=UTF-8
"""
Módulo: Testa a classe da modalidade de competição Arremesso de Peso das
olimpíadas.
"""
import unittest
from tests.utils import MockInput
from ooppython3.modalidadearremessopeso import ArremessoPeso, \
    ARREMESSO_NUMERO_ADVERSARIOS, NUMERO_ARREMESSOS
from ooppython3.adversarioarremessopeso import AdversarioArremessoPeso


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
        self.assertEqual(ap.lerentrada(numadversario="1"),
                         '1.0,2.0,3.0',
                         "Esperada string '1.0,2.0,3.0'")

    def test_validar_entrada_valida(self):
        """
        Testa os parâmetros do construtor da classe.

        :return: None
        """
        inp = MockInput("1.0,2.0,3.0")
        ap = ArremessoPeso(inp=inp)
        ret = ap.validarentrada(
            entrada=ap.lerentrada(numadversario="1")
        )
        self.assertEqual(ret,
                         True,
                         "Função deveria ter retornado True")

    def test_validar_entrada_arremessos_a_menos(self):
        """
        Testa os parâmetros do construtor da classe.

        :return: None
        """
        inp = MockInput("1.0,2.0")
        ap = ArremessoPeso(inp=inp)
        ret = ap.validarentrada(
            entrada=ap.lerentrada(numadversario="1")
        )
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
        ret = ap.validarentrada(
            entrada=ap.lerentrada(numadversario="1")
        )
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
        ret = ap.validarentrada(
            entrada=ap.lerentrada(numadversario="1")
        )
        self.assertEqual(ret,
                         False,
                         "Função deveria ter retornado False")

    def test_numero_adversarios(self):
        """
        Testa os parâmetros do construtor da classe.

        :return: None
        """
        inp = MockInput("")
        ap = ArremessoPeso(inp=inp)
        self.assertEqual(ap.numeroadversarios(),
                         ARREMESSO_NUMERO_ADVERSARIOS,
                         "Função deveria ter retornado {} adversarios".format(
                             ARREMESSO_NUMERO_ADVERSARIOS)
                         )

    def test_validar_empate_simples(self):
        """
        Testa os parâmetros do construtor da classe.

        :return: None
        """
        ap = ArremessoPeso(inp=MockInput(""))
        ap._adversarios = [
            AdversarioArremessoPeso(
                nome="Adversario 1", resultado=[1.0, 2.0, 3.0]),
            AdversarioArremessoPeso(
                nome="Adversario 2", resultado=[1.0, 2.0, 3.0])
        ]
        ap.iniciar()
        self.assertEqual(ap.vencedor(),
                         "Empate",
                         "Deveria haver um empate.")

    def test_validar_desempate_simples_vencedor_1(self):
        """
        Testa os parâmetros do construtor da classe.

        :return: None
        """
        ap = ArremessoPeso(inp=MockInput(""))
        ap._adversarios = [
            AdversarioArremessoPeso(
                nome="Adversario 1", resultado=[1.0, 2.0, 4.0]),
            AdversarioArremessoPeso(
                nome="Adversario 2", resultado=[1.0, 2.0, 3.0])
        ]
        ap.iniciar()
        self.assertEqual(ap.vencedor(),
                         "Adversario 1",
                         "Adversario 1 deveria ser o vencedor.")

    def test_validar_desempate_simples_vencedor_2(self):
        """
        Testa os parâmetros do construtor da classe.

        :return: None
        """
        ap = ArremessoPeso(inp=MockInput(""))
        ap._adversarios = [
            AdversarioArremessoPeso(
                nome="Adversario 1", resultado=[1.0, 2.0, 3.0]),
            AdversarioArremessoPeso(
                nome="Adversario 2", resultado=[1.0, 2.0, 4.0])
        ]
        ap.iniciar()
        self.assertEqual(ap.vencedor(),
                         "Adversario 2",
                         "Adversario 2 deveria ser o vencedor.")

    def test_validar_desempate_segunda_melhor_marca_vencedor_1(self):
        """
        Testa os parâmetros do construtor da classe.

        :return: None
        """
        ap = ArremessoPeso(inp=MockInput(""))
        ap._adversarios = [
            AdversarioArremessoPeso(
                nome="Adversario 1", resultado=[1.0, 2.0, 3.0]),
            AdversarioArremessoPeso(
                nome="Adversario 2", resultado=[1.0, 1.0, 3.0])
        ]
        ap.iniciar()
        self.assertEqual(ap.vencedor(),
                         "Adversario 1",
                         "Adversario 1 deveria ser o vencedor.")

    def test_validar_desempate_segunda_melhor_marca_vencedor_2(self):
        """
        Testa os parâmetros do construtor da classe.

        :return: None
        """
        ap = ArremessoPeso(inp=MockInput(""))
        ap._adversarios = [
            AdversarioArremessoPeso(
                nome="Adversario 1", resultado=[1.0, 1.0, 3.0]),
            AdversarioArremessoPeso(
                nome="Adversario 2", resultado=[1.0, 2.0, 3.0])
        ]
        ap.iniciar()
        self.assertEqual(ap.vencedor(),
                         "Adversario 2",
                         "Adversario 2 deveria ser o vencedor.")
