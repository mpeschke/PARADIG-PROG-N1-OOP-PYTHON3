# coding=UTF-8
"""
Módulo: Fornece um menu para as modalidades de competição disponíveis, além
de ler e analisar as entradas.
"""
from ooppython3.utils import DynamicClassLoaderModalidade
from ooppython3.modalidadearremessopeso import ID_MODALIDADE_ARREMESSOPESO
from ooppython3.modalidadeginasticaartistica import \
    ID_MODALIDADE_GINASTICAARTISTICA

ENTRADA_MODALIDADE_MENSAGEM = "Digite o número da modalidade (1-Arremesso de" \
                              " Peso, 2-Ginástica Artística): "


class Menu:
    """
    Gerencia a escolha, validação e execução das modalidades de competições
    da Olimpíada.
    """
    modalidades = [
        {
            "id": ID_MODALIDADE_ARREMESSOPESO,
            "modalidademodule": "ooppython3.modalidadearremessopeso",
            "modalidadeclass": "ArremessoPeso"
        },
        {
            "id": ID_MODALIDADE_GINASTICAARTISTICA,
            "modalidademodule": "ooppython3.modalidadeginasticaartistica",
            "modalidadeclass": "GinasticaArtistica"
        },
    ]
    modalidadeid = None
    _input = None

    def __init__(self, inp):
        """
        Construtor
        @param inp: instância da classe responsável pela entrada de dados.
        """
        self._input = inp

    def lerentrada(self):
        """
        Coleta a entrada (identificação) da modalidade escolhida.
        @return: a entrada selecionada
        """
        self.modalidadeid = self._input.input(ENTRADA_MODALIDADE_MENSAGEM)

    def validarmodalidade(self):
        """
        Retorna uma lista com os resultados de um filtro que tenta localizar
        modalidades pelo id. Se a lista estiver vazia, não encontrou.
        @return: True (modalidade implementada) ou
        False (modalidade desconhecida)
        """
        if self.modalidadeid is None:
            return False

        return len(
            list(
                filter(lambda mod: mod['id'] == self.modalidadeid,
                       self.modalidades)
            )
        ) != 0

    def modalidade(self, inp):
        """
        Instancia a classe da modalidade de competição olímpica.
        @param inp: instância da classe responsável pela entrada de dados.
        @return: instância da classe da modalidade.
        """
        modulo = list(
            filter(
                lambda mod: mod['id'] == self.modalidadeid,
                self.modalidades
            )
        )[0]["modalidademodule"]
        classe = list(filter(
            lambda mod: mod['id'] == self.modalidadeid,
            self.modalidades
        ))[0]["modalidadeclass"]
        return DynamicClassLoaderModalidade.instancia(modulo, classe, inp)
