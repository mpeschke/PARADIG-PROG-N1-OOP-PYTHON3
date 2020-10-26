# coding=UTF-8
"""
Módulo: Representa um adversário na competição Arremesso de Peso.
"""
from ooppython3.adversario import Adversario


class AdversarioArremessoPeso(Adversario):
    """
    Classe representando um competidor na modalidade Arremesso de Peso.
    """
    def __init__(self, nome, resultado):
        super(AdversarioArremessoPeso, self).__init__(nome, resultado)
