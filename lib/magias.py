from system.efeitos import *


class Magia:
    def __init__(self,
                 nome: str,
                 dano: list,
                 tipo: str,
                 custo: int,
                 duracao: int,
                 efeitos: list or object):
        self.nome = nome
        self.dano = dano
        self.tipo = tipo
        self.custo = custo
        self.duracao = duracao  # Em turnos
        self.efeitos = efeitos


# Magias prontas
Magia(nome="Bola de Fogo",
      dano=[6, 12],
      tipo="fogo",
      custo=4,
      duracao=1,
      efeitos=EfeitoMagico.incendiar)
