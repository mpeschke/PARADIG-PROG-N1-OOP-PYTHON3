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
        """
        Construtor
        @param inp: instância da classe responsável pela entrada de dados.
        """
        super(GinasticaArtistica, self).__init__(
            inp,
            numtentativas=NUMERO_NOTAS,
            numadversarios=GINASTICA_NUMERO_ADVERSARIOS,
            mensagem=MENSAGEM_LER_NOTAS
        )

    def iniciar(self):
        """
        Processamento da competição de Ginástica Artística.
        @return:
        """
        # Primeiro passo, ordena as marcas (resultados) individuais dos
        # adversários.
        super(GinasticaArtistica, self).iniciar()

        # Segundo passo, exclui o pior resultado, calcula as médias das notas
        # e cria um dicionário com as médias dos adversários.
        melhoresnotas = {
            self.adversarios()[0].nome():
                sum(nota for nota in
                    self.adversarios()[0].resultado()[
                        0:len(self.adversarios()[0].resultado())-1]
                    ),
            self.adversarios()[1].nome():
                sum(nota for nota in
                    self.adversarios()[1].resultado()[
                        0:len(self.adversarios()[1].resultado())-1]
                    ),
        }
        # Terceiro passo, ordena os dois melhores resultados do adversários
        # e verifica se há um vencedor.
        melhoresnotas = {
            k: v for k,
            v in sorted(
                melhoresnotas.items(),
                key=lambda item: item[1],
                reverse=True
            )
        }
        if len(set(melhoresnotas.values())) > 1:
            self._vencedor = list(melhoresnotas.keys())[0]
            return
