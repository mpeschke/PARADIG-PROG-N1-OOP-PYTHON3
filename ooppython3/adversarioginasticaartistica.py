# coding=UTF-8
"""
Módulo: Representa um adversário na competição Ginástica Artística.
"""
from ooppython3.adversario import Adversario


class AdversarioGinasticaArtistica(Adversario):
    """
    Classe representando um competidor na modalidade Ginástica Artística.
    """
    def __init__(self, nome, resultado):
        super(AdversarioGinasticaArtistica, self).__init__(nome, resultado)
