# coding=UTF-8
"""
Módulo: Fornece a superclasse com todos os métodos necessários para
implementar uma modalidade de competição de olimpíadas.
"""
from ooppython3.adversario import Adversario


class Modalidade:
    """
    Superclasse representando uma modalidade de competição das olimpíadas.
    """
    _adversarios = []
    _input = None
    _numtentativas = None
    _numadversarios = None
    _mensagem = None
    _vencedor = "Empate"

    def __init__(self, inp, numtentativas, numadversarios, mensagem):
        self._input = inp
        self._numtentativas = numtentativas
        self._numadversarios = numadversarios
        self._mensagem = mensagem

    def lerentrada(self, numadversario):
        return self._input.input(
                self._mensagem.format(
                    self._numtentativas, numadversario
                )
        )

    def validarentrada(self, entrada):
        if len(self._adversarios) is self._numadversarios:
            return False

        _strtentativas = entrada.split(',')
        if len(_strtentativas) < self._numtentativas:
            return False

        try:
            _floattentativas = [float(x) for x in _strtentativas]
        except ValueError:
            return False

        if len(_floattentativas) is self._numtentativas:
            self._adversarios.append(
                Adversario(
                    nome="Adversario {}".format(len(self._adversarios)+1),
                    resultado=_floattentativas
                )
            )
            return True
        else:
            return False

    def iniciar(self):
        for adversario in self.adversarios():
            adversario.resultado().sort(reverse=True)

    def numeroadversarios(self):
        return self._numadversarios

    def numerotentativas(self):
        return self._numtentativas

    def adversarios(self):
        return self._adversarios

    def vencedor(self):
        return self._vencedor
