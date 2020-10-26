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


class ArremessoPeso(Modalidade):
    """
    Classe representando a modalidade de competição Arremesso de Peso.
    """
    arremessos = None

    def __init__(self, inp):
        super(ArremessoPeso, self).__init__(inp)

    def lerentrada(self):
        self._entrada = self._input.input(
            MENSAGEM_LER_ARREMESSOS.format(NUMERO_ARREMESSOS, "1")
        )

    def validarentrada(self):
        if self._entrada is None:
            return False

        _arremessos = self._entrada.split(',')
        if len(_arremessos) < NUMERO_ARREMESSOS:
            return False

        try:
            self.arremessos = [float(x) for x in _arremessos]
        except ValueError:
            return False

        return len(self.arremessos) is NUMERO_ARREMESSOS

    def iniciarmodalidade(self):
        pass

    def iniciar(self):
        pass

    def vencedor(self):
        pass
