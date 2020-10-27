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
        """
        Construtor.
        @param inp: instância da classe responsável pela entrada de dados.
        @param numtentativas: número de tentativas (notas, arremessos) para
        classificação na competição.
        @param numadversarios: número de adversários na competição.
        @param mensagem: Mensagem fornecida pra orientar a entrada de dados.
        """
        self._input = inp
        self._numtentativas = numtentativas
        self._numadversarios = numadversarios
        self._mensagem = mensagem

    def validarentrada(self, entrada):
        """
        Valida a entrada de dados (notas, arremessos) do adversário.
        @param entrada: (notas, arremessos) do adversário.
        @return: True (válidas) ou False (inválidas).
        """
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
        return False

    def lerentrada(self, numadversario):
        """
        Captura a entrada de dados do usuário.
        @param numadversario: identificador do adversário.
        @return: entrada de dados do usuário.
        """
        return self._input.input(
            self._mensagem.format(
                self._numtentativas, numadversario
            )
        )

    def iniciar(self):
        """
        Executa a competição (processa os resultados).
        Notar que a superclasse processa apenas uma parte comum a todas as
        competições, que é ordenar os resultados.
        @return: None
        """
        for adversario in self.adversarios():
            adversario.resultado().sort(reverse=True)

    def numeroadversarios(self):
        """
        Número de adversários.
        @return: número de adversários.
        """
        return self._numadversarios

    def numerotentativas(self):
        """
        Número de tentativas (notas, arremessos)
        @return: número de tentativas (notas, arremessos).
        """
        return self._numtentativas

    def adversarios(self):
        """
        Lista de adversários na competição.
        @return: lista de adversários (instâncias 'adversario').
        """
        return self._adversarios

    def vencedor(self):
        """
        Vencedor da competição.
        @return: Nome do vencedor (adversário) ou 'Empate' em caso de empate.
        """
        return self._vencedor
