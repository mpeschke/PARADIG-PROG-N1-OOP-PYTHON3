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


class GinasticaArtistica(Modalidade):
    """
    Classe representando a modalidade de competição de Ginástica Artística.
    """
    notas = None

    def __init__(self, inp):
        super(GinasticaArtistica, self).__init__(inp)

    def lerentrada(self):
        self._entrada = self._input.input(
            MENSAGEM_LER_NOTAS.format(NUMERO_NOTAS, "1")
        )

    def validarentrada(self):
        if self._entrada is None:
            return False

        _notas = self._entrada.split(',')
        if len(_notas) < NUMERO_NOTAS:
            return False

        try:
            self.notas = [float(x) for x in _notas]
        except ValueError:
            return False

        return len(self.notas) is NUMERO_NOTAS

    def iniciarmodalidade(self):
        pass

    def iniciar(self):
        pass

    def vencedor(self):
        pass
