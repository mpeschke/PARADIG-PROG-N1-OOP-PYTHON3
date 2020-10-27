# coding=UTF-8
"""
Módulo: Fornece classe com todos os métodos necessários para
implementar uma modalidade de competição de Ginástica Artística.
"""
from ooppython3.modalidade import Modalidade
from ooppython3.adversarioginasticaartistica import \
    AdversarioGinasticaArtistica
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
        super(GinasticaArtistica, self).__init__(inp)

    def lerentrada(self, numadversario):
        return self._input.input(
            MENSAGEM_LER_NOTAS.format(
                NUMERO_NOTAS, numadversario
            )
        )

    def validarentrada(self, entrada):
        if len(self._adversarios) is GINASTICA_NUMERO_ADVERSARIOS:
            return False

        _strnotas = entrada.split(',')
        if len(_strnotas) < NUMERO_NOTAS:
            return False

        try:
            _floatnotas = [float(x) for x in _strnotas]
        except ValueError:
            return False

        if len(_floatnotas) is NUMERO_NOTAS:
            self._adversarios.append(
                AdversarioGinasticaArtistica(
                    nome="Adversario {}".format(len(self._adversarios)+1),
                    resultado=_floatnotas
                )
            )
            return True
        else:
            return False

    def iniciarmodalidade(self):
        pass

    def iniciar(self):
        pass

    def numeroadversarios(self):
        return GINASTICA_NUMERO_ADVERSARIOS

    def vencedor(self):
        pass
