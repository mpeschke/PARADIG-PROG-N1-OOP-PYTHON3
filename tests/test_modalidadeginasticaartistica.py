# coding=UTF-8
"""
Módulo: Testa a classe da modalidade de competição Ginástica Artística das
olimpíadas.
"""
import unittest
from tests.utils import MockInput
from ooppython3.modalidadeginasticaartistica import GinasticaArtistica, \
    GINASTICA_NUMERO_ADVERSARIOS
from ooppython3.adversarioginasticaartistica import \
    AdversarioGinasticaArtistica


class TestModalidadeGinasticaArtistica(unittest.TestCase):
    """
    Suíte de testes da classe representando a modalidade de competição
    Ginástica Artística das olimpíadas.
    Notar o uso da classe MockInput para simular a entrada de dados
    sem o bloqueio do stadin real.
    """
    def test_ler_entrada(self):
        """
        Testa cenário de entrada correta (usuário digita valores válidos de
        notas).
        :return: None
        """
        ap = GinasticaArtistica(inp=MockInput("1.0,2.0,3.0,4.0,5.0"))
        self.assertEqual(ap.lerentrada(numadversario="1"),
                         '1.0,2.0,3.0,4.0,5.0',
                         "Esperada string '1.0,2.0,3.0,4.0,5.0'")

    def test_validar_entrada_valida(self):
        """
        Testa cenário de entrada correta (usuário digita valores válidos de
        notas).
        :return: None
        """
        ap = GinasticaArtistica(inp=MockInput("1.0,2.0,3.0,4.0,5.0"))
        ret = ap.validarentrada(
            entrada=ap.lerentrada(numadversario="1")
        )
        self.assertEqual(ret,
                         True,
                         "Função deveria ter retornado True")

    def test_validar_entrada_notas_a_menos(self):
        """
        Testa cenário de entrada incorreta (usuário digita menos valores de
        notas que o esperado).
        :return: None
        """
        ap = GinasticaArtistica(inp=MockInput("1.0,2.0"))
        ret = ap.validarentrada(
            entrada=ap.lerentrada(numadversario="1")
        )
        self.assertEqual(ret,
                         False,
                         "Função deveria ter retornado False")

    def test_validar_entrada_notas_a_mais(self):
        """
        Testa cenário de entrada incorreta (usuário digita valores de
        notas a mais que o esperado).
        :return: None
        """
        ap = GinasticaArtistica(inp=MockInput("1.0,2.0,3.0,4.0,5.0,6.0"))
        ret = ap.validarentrada(
            entrada=ap.lerentrada(numadversario="1")
        )
        self.assertEqual(ret,
                         False,
                         "Função deveria ter retornado False")

    def test_validar_entrada_invalida(self):
        """
        Testa cenário de entrada incorreta (usuário digita valores de
        notas inválidos).
        :return: None
        """
        ap = GinasticaArtistica(inp=MockInput("1.0,invalido,3.0,4.0,5.0"))
        ret = ap.validarentrada(
            entrada=ap.lerentrada(numadversario="1")
        )
        self.assertEqual(ret,
                         False,
                         "Função deveria ter retornado False")

    def test_numero_adversarios(self):
        """
        Testa cenário de número de adversários incorreto (houve alguma
        confusão na chamada das funções da modalidade pela classe Menu).
        :return: None
        """
        ap = GinasticaArtistica(inp=MockInput(""))
        self.assertEqual(ap.numeroadversarios(),
                         GINASTICA_NUMERO_ADVERSARIOS,
                         "Função deveria ter retornado {} adversarios".format(
                             GINASTICA_NUMERO_ADVERSARIOS)
                         )

    def test_validar_empate_simples_1(self):
        """
        Testa cenário de empate na competição (média igual de notas).
        :return: None
        """
        ap = GinasticaArtistica(inp=MockInput(""))
        ap._adversarios = [
            AdversarioGinasticaArtistica(
                nome="Adversario 1", resultado=[1.0, 2.0, 3.0, 4.0, 5.0]),
            AdversarioGinasticaArtistica(
                nome="Adversario 2", resultado=[1.0, 2.0, 3.0, 4.0, 5.0])
        ]
        ap.iniciar()
        self.assertEqual(ap.vencedor(),
                         "Empate",
                         "Deveria haver um empate.")

    def test_validar_empate_simples_2(self):
        """
        Testa cenário de empate na competição (média igual de notas).
        :return: None
        """
        ap = GinasticaArtistica(inp=MockInput(""))
        ap._adversarios = [
            AdversarioGinasticaArtistica(
                nome="Adversario 1", resultado=[1.0, 3.0, 3.0, 8.0, 10.0]),
            AdversarioGinasticaArtistica(
                nome="Adversario 2", resultado=[1.0, 3.0, 6.0, 10.0, 5.0])
        ]
        ap.iniciar()
        self.assertEqual(ap.vencedor(),
                         "Empate",
                         "Deveria haver um empate.")

    def test_validar_desempate_simples_vencedor_1(self):
        """
        Testa cenário de vencedor na competição (adversário #1).
        :return: None
        """
        ap = GinasticaArtistica(inp=MockInput(""))
        ap._adversarios = [
            AdversarioGinasticaArtistica(
                nome="Adversario 1", resultado=[1.0, 2.0, 3.0, 4.0, 5.0]),
            AdversarioGinasticaArtistica(
                nome="Adversario 2", resultado=[1.0, 2.0, 3.0, 4.0, 4.9])
        ]
        ap.iniciar()
        self.assertEqual(ap.vencedor(),
                         "Adversario 1",
                         "Adversario 1 deveria ser o vencedor.")

    def test_validar_desempate_simples_vencedor_2(self):
        """
        Testa cenário de vencedor na competição (adversário #2).
        :return: None
        """
        ap = GinasticaArtistica(inp=MockInput(""))
        ap._adversarios = [
            AdversarioGinasticaArtistica(
                nome="Adversario 1", resultado=[1.0, 2.0, 3.0, 4.0, 4.9]),
            AdversarioGinasticaArtistica(
                nome="Adversario 2", resultado=[1.0, 2.0, 3.0, 4.0, 5.0])
        ]
        ap.iniciar()
        self.assertEqual(ap.vencedor(),
                         "Adversario 2",
                         "Adversario 2 deveria ser o vencedor.")

    def test_validar_desempate_elimina_pior_nota_vencedor_1(self):
        """
        Testa cenário de vencedor na competição (adversário #1).
        :return: None
        """
        ap = GinasticaArtistica(inp=MockInput(""))
        ap._adversarios = [
            AdversarioGinasticaArtistica(
                nome="Adversario 1", resultado=[0.0, 4.0, 4.0, 6.0, 9.0]),
            AdversarioGinasticaArtistica(
                nome="Adversario 2", resultado=[4.0, 4.0, 4.0, 4.0, 10.0])
        ]
        ap.iniciar()
        self.assertEqual(ap.vencedor(),
                         "Adversario 1",
                         "Adversario 1 deveria ser o vencedor.")

    def test_validar_desempate_elimina_pior_nota_vencedor_2(self):
        """
        Testa cenário de vencedor na competição (adversário #2).
        :return: None
        """
        ap = GinasticaArtistica(inp=MockInput(""))
        ap._adversarios = [
            AdversarioGinasticaArtistica(
                nome="Adversario 1", resultado=[4.0, 4.0, 4.0, 4.0, 10.0]),
            AdversarioGinasticaArtistica(
                nome="Adversario 2", resultado=[0.0, 4.0, 4.0, 6.0, 9.0])
        ]
        ap.iniciar()
        self.assertEqual(ap.vencedor(),
                         "Adversario 2",
                         "Adversario 2 deveria ser o vencedor.")
