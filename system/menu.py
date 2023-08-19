from system.hud import Hud
from system.text import Fore, Style


class Tela:
    def __init__(self, char, inimigos, companios=None):
        self.char = char
        self.inimigos = inimigos
        self.companios = companios

    def telaCombate(self):
        # Mostrar barras de status do personagem
        Hud.lifeHud(self.char)

        # Mostrar menu de combate
        chance_fuga = Hud.calcularChance(
            atributo_p=self.char.atributos_p['MISTICO'],
            atributo_s=self.char.atributos_s['sor'])

        # Verificar se há Companions
        # Exibir Menu de Escolha de Ações
        if self.companios is None:
            Menu.botao(
                escolhas=("Atacar",
                          "Defender",
                          "Itens",
                          "Magias",
                          f"Fugir {Fore.YELLOW + Style.DIM}{chance_fuga[0]}%{Style.RESET_ALL}"),
                botoes=(self.telaAtaque, self.telaDefesa)
            )
        else:
            Menu.botao(
                escolhas=("Atacar",
                          "Defender",
                          "Itens",
                          "Magias",
                          "Aliados",
                          f"Fugir {Fore.YELLOW + Style.DIM}{chance_fuga[0]}%{Style.RESET_ALL}"),
                botoes=()
            )
        # Mostrar log de combates

    def telaAtaque(self):
        Menu.botao(escolhas=(f"{self.char.equipamento['arma']['nome']}",
                             "Trocar de Arma"),
                   botoes=(), voltar=True)

    def telaDefesa(self):
        Menu.botao(escolhas=("Postura Defensiva",
                             "Preparar Contra-Ataque"),
                   botoes=(), voltar=True)


class Menu:
    @staticmethod
    def escolha(opcoes: tuple) -> tuple:
        # Laço de Repetição + tratamento de Erro
        while True:
            try:
                # Mostra as opções na tela
                for numero, opcao in enumerate(opcoes):
                    print(f"[{numero + 1}] {opcao}")

                escolha = int(input(">> "))
                if 0 < escolha <= len(opcoes):
                    break
                else:
                    Hud.opcaoNaoExiste()
            except ValueError:
                Hud.opcaoNaoExiste()

        # Retorna o endereço e a oção
        return escolha - 1, opcoes[escolha - 1]

    @staticmethod
    def botao(escolhas: tuple, botoes: tuple, voltar=False):
        # Adiciona a opção "Voltar"
        if voltar is True:
            lista_escolhas = list(escolhas)
            lista_escolhas.append("Voltar")
            escolhas = tuple(lista_escolhas)
        resposta = Menu.escolha(escolhas)

        # Verifica se foi escolhida a opção voltar
        if voltar is True and resposta[0] == len(escolhas)-1:
            return 'voltar'

        # Executa uma das funções na ordem
        botoes[resposta[0]]()
