from math import floor, ceil

from system.text import Fore
from time import sleep


class Hud:
    @staticmethod
    def lifeHud(char):
        # =================[Barra dos PVs]===========================
        barra_var = char.status_atual['PV'] * 40 / char.status['PV']
        if barra_var > 0:
            barra_fixa = 40 - barra_var
        else:
            barra_fixa = 40
        print('PV: ', Fore.RED + '█' * floor(barra_var), end='')
        print(Fore.BLACK + '█' * ceil(barra_fixa), Fore.RESET + f'{char.status["PV"]} ({char.status_atual["PV"]})')
        # =================[Barra dos PAs]===========================
        barra_var = char.status_atual['PA'] * 40 / char.status['PA']
        barra_fixa = 40 - barra_var
        print('PA: ', Fore.BLUE + '█' * floor(barra_var), end='')
        print(Fore.BLACK + '█' * ceil(barra_fixa), Fore.RESET +
              f'{char.status["PA"]} ({char.status_atual["PA"]})' + Fore.RESET)
        # =================[Barra dos PEs]===========================
        barra_var = char.status_atual['PE'] * 40 / char.status['PE']
        barra_fixa = 40 - barra_var
        print('PE: ', Fore.CYAN + '█' * floor(barra_var), end='')
        print(Fore.BLACK + '█' * ceil(barra_fixa), Fore.RESET +
              f'{char.status["PE"]} ({char.status_atual["PE"]})' + Fore.RESET)

    @staticmethod
    def msgDano(alvo_nome, dano, tipo=None):
        if tipo is not None:
            print(f'{alvo_nome} sofreu {dano} de dano de {tipo}!\n')
            sleep(0.3)
        else:
            print(f'{alvo_nome} sofreu {dano} de dano!\n')
            sleep(0.3)

    @staticmethod
    def calcularChance(atributo_p: int, atributo_s: int) -> tuple[int, int]:
        chance_sucesso = (atributo_p+atributo_s)*5
        chance_fracasso = (20-atributo_p-atributo_s)*5

        return chance_sucesso, chance_fracasso

    @staticmethod
    def opcaoNaoExiste():
        print(Fore.RED + 'Não existe essa opção! Selecione outra.' + Fore.RESET)
