# coding=UTF-8
"""
Módulo: Fornece um menu para as modalidades de competição disponíveis, além
de ler as entradas e processar o vencedor.
"""
from ooppython3.input import Input
from ooppython3.menu import Menu


def main():
    """
    Entrada da aplicação. Pergunta pelo tipo de competição, executa e mostra
    o resultado final.
    @return: 0 (sucesso) ou 1 (erro)
    """
    inp = Input()
    menu = Menu(inp)
    # Valida e recebe a identificação de qual modalidade será executada.
    while not menu.validarmodalidade():
        menu.lerentrada()

    modalidade = menu.modalidade(inp)

    # Valida e recebe os resultados de todos os adversários da modalidade.
    for numadversario in range(modalidade.numeroadversarios()):
        while not modalidade.validarentrada(
                modalidade.lerentrada(numadversario+1)
        ):
            continue

    # Processa o resultado (vencedor).
    modalidade.iniciar()

    print("Vencedor: {}".format(modalidade.vencedor()))


if __name__ == '__main__':
    main()
