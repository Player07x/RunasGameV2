from system.hud import Hud


class Tela:
    def telaCombate(self):
        pass
        # Mostrar barras de status do personagem
        # Mostrar menu de combate
        # Mostrar log de combate


class Menu:
    @staticmethod
    def escolha(opcoes: tuple) -> tuple:
        # Laço de Repetição + tratamento de Erro
        while True:
            try:
                # Mostra as opções na tela
                for numero, opcao in enumerate(opcoes):
                    print(f"[{numero+1}] {opcao}")

                escolha = int(input(">> "))
                if 0 < escolha <= len(opcoes):
                    break
                else:
                    Hud.opcaoNaoExiste()
            except ValueError:
                Hud.opcaoNaoExiste()

        # Retorna o endereço e a oção
        return escolha-1, opcoes[escolha-1]

    @staticmethod
    def botao(escolhas: tuple, botoes: tuple):
        resposta = Menu.escolha(escolhas)
        # Executa uma das funções na ordem
        botoes[resposta[0]]()
