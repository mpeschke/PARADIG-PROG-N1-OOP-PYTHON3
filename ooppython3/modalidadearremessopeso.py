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
        """
        Construtor
        @param inp: instância da classe responsável pela entrada de dados.
        """
        super(ArremessoPeso, self).__init__(
            inp,
            numtentativas=NUMERO_ARREMESSOS,
            numadversarios=ARREMESSO_NUMERO_ADVERSARIOS,
            mensagem=MENSAGEM_LER_ARREMESSOS
        )

    def iniciar(self):
        """
        Processamento da competição de arremesso de peso.
        @return:
        """
        # Primeiro passo, ordena as marcas (resultados) individuais dos
        # adversários.
        super(ArremessoPeso, self).iniciar()

        # Procuramos por vencedores nos melhores ou nos segundos melhores
        # arremessos.
        for i in range(2):
            melhoresarremessos = {
                self.adversarios()[0].nome():
                    self.adversarios()[0].resultado()[i],
                self.adversarios()[1].nome():
                    self.adversarios()[1].resultado()[i]
            }
            # Segundo passo, ordena os dois melhores resultados do adversários
            # e verifica se há um vencedor.
            melhoresarremessos = {
                k: v for k,
                v in sorted(
                    melhoresarremessos.items(),
                    key=lambda item: item[1],
                    reverse=True
                )
            }
            # Terceiro passo, aproveitando a característica de 'set' ter apenas
            # elementos únicos, identificamos ou não um empate.
            if len(set(melhoresarremessos.values())) > 1:
                self._vencedor = list(melhoresarremessos.keys())[0]
                return
