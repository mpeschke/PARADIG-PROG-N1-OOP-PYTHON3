# coding=UTF-8
"""
Módulo: Fornece classe com todos os métodos necessários para
implementar uma modalidade de competição de Ginástica Artística.
"""
from ooppython3.modalidade import Modalidade
MENSAGEM_LER_NOTAS = "Entre com as {} notas do adversário {}: (Exemplo: 9.7," \
                     "10.0,...): "
NUMERO_NOTAS = 5
GINASTICA_NUMERO_ADVERSARIOS = 2
ID_MODALIDADE_GINASTICAARTISTICA = "2"


class GinasticaArtistica(Modalidade):
    """
    Classe representando a modalidade de competição de Ginástica Artística.
    """
    def __init__(self, inp):
        super(GinasticaArtistica, self).__init__(
            inp,
            numtentativas=NUMERO_NOTAS,
            numadversarios=GINASTICA_NUMERO_ADVERSARIOS,
            mensagem=MENSAGEM_LER_NOTAS
        )

    def lerentrada(self, numadversario):
        return super(GinasticaArtistica, self).lerentrada(
            numadversario=numadversario
        )

    def validarentrada(self, entrada):
        return super(GinasticaArtistica, self).validarentrada(entrada=entrada)

    def iniciar(self):
        pass

    def vencedor(self):
        pass
