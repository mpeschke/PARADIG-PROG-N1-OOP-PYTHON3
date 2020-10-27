# coding=UTF-8
"""
Módulo: Fornece classe com todos os métodos necessários para
implementar uma modalidade de competição de Arremesso de Peso.
"""
from ooppython3.modalidade import Modalidade
from ooppython3.adversarioarremessopeso import AdversarioArremessoPeso

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
        super(ArremessoPeso, self).__init__(inp)

    def lerentrada(self, numadversario):
        return self._input.input(
            MENSAGEM_LER_ARREMESSOS.format(
                NUMERO_ARREMESSOS, numadversario
            )
        )

    def validarentrada(self, entrada, numadversarios, numtentativas):
        return super(ArremessoPeso, self).validarentrada(
            entrada=entrada,
            numadversarios=numadversarios,
            numtentativas=numtentativas
        )

    def iniciarmodalidade(self):
        pass

    def iniciar(self):
        pass

    def numeroadversarios(self):
        return ARREMESSO_NUMERO_ADVERSARIOS

    def vencedor(self):
        pass
