from system.menu import Tela
from lib.char import Character
from system.hud import Hud

if __name__ == '__main__':
    char = Character()
    char.setAtributos(atributo_p=[8, 8, 8],
                             atributo_s=[2, 4, 2,
                                         2, 4, 2,
                                         2, 4, 2])
    char.setStatus(atual=True)

    Tela(char, char).telaCombate()
