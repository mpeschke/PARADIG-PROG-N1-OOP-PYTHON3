# coding=UTF-8
"""
Módulo: Fornece um menu para as modalidades de competição disponíveis, além
de ler e analisar as entradas.
"""
from ooppython3.input import Input
from ooppython3.menu import Menu


def main():
    """
    Entrada da aplicação. Pergunta pelo tipo de competição, executa e mostra
    o resultado final.
    :return: int ErrorCode ou 0 (Successo)
    """
    inp = Input()
    menu = Menu(inp)
    while not menu.validarmodalidade():
        menu.lerentrada()

    modalidade = menu.modalidade(inp)

    for numadversario in range(modalidade.numeroadversarios()):
        while not modalidade.validarentrada(
                modalidade.lerentrada(numadversario+1)
        ):
            continue

    modalidade.iniciar()

    print("Vencedor: {}".format(modalidade.vencedor()))


if __name__ == '__main__':
    main()
