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
            numadversarios=ARREMESSO_NUMERO_ADVERSARIOS
        )

    def lerentrada(self, numadversario):
        return self._input.input(
                MENSAGEM_LER_ARREMESSOS.format(
                    NUMERO_ARREMESSOS, numadversario
                )
        )

    def validarentrada(self, entrada):
        return super(ArremessoPeso, self).validarentrada(entrada=entrada)

    def iniciarmodalidade(self):
        pass

    def iniciar(self):
        pass

    def vencedor(self):
        pass
