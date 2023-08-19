class Turno:

    def __init__(self, jogador, inimigos, companions=None):
        self.jogador = None
        self.inimigos = None
        self.companions = None

    def turnoGeral(self):
        Turno.turnoJogador(self)
        Turno.turnoIA(self)

    def turnoJogador(self):
        # Aplicar Efeitos do Jogador
        # Menu de Combate
        # Fim do turno
        pass

    def turnoIA(self):
        # Turno dos Inimigos
        for inim in self.inimigos:
            # Aplicar Efeito no Inimigo
            if self.jogador.status_atual['PV'] <= 0:
                return False

        # Turno dos Companions
        if self.companions is not None and self.jogador.status_atual['PV'] > 0:
            for ali in self.companions:
                pass
