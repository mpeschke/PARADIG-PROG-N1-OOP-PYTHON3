# coding=UTF-8
"""
Módulo: Fornece classe com todos os métodos necessários para
implementar uma modalidade de competição de Arremesso de Peso.
"""
from ooppython3.modalidade import Modalidade

MENSAGEM_LER_ARREMESSOS = "Entre com os {} arremessos do adversário {}: (Exe" \
                          "mplo: 9.7,10.0,...): "
NUMERO_ARREMESSOS = 3
ARREMESSO_NUMERO_ADVERSARIOS = 2
ID_MODALIDADE_ARREMESSOPESO = "1"


class ArremessoPeso(Modalidade):
    """
    Classe representando a modalidade de competição Arremesso de Peso.
    """
    def __init__(self, inp):
        super(ArremessoPeso, self).__init__(
            inp,
            numtentativas=NUMERO_ARREMESSOS,
            numadversarios=ARREMESSO_NUMERO_ADVERSARIOS,
            mensagem=MENSAGEM_LER_ARREMESSOS
        )

    def lerentrada(self, numadversario):
        return super(ArremessoPeso, self).lerentrada(
            numadversario=numadversario
        )

    def validarentrada(self, entrada):
        return super(ArremessoPeso, self).validarentrada(entrada=entrada)

    def iniciar(self):
        # Primeiro passo, ordenar os resultados dos adversários.
        super(ArremessoPeso).iniciar()

        # Segundo passo, vence de primeira o que tiver a melhor marca.


    def vencedor(self):
        pass
