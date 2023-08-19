from math import ceil, floor
from random import randint
from system.hud import Hud


class Combate:
    @staticmethod
    def danoGeral(alvo, dano):
        # Se PA é 0, causar dano nos PVs
        if alvo.status_atual['PA'] <= 0:
            alvo.status_atual['PV'] -= dano
        # Se não, causar dano nos PAs
        else:
            alvo.status_atual['PA'] -= dano
            dano_excedente = alvo.status_atual['PA']
            # Se o dano for maior que os PAs, zerar os PAs
            # Causar metade do dano excedente nos PVs
            if alvo.status_atual['PA'] <= 0:
                alvo.status_atual['PA'] = 0
                alvo.status_atual['PV'] += ceil(dano_excedente / 2)

    @staticmethod
    def danoFisico(alvo, dano: list, tipo: str, efeito=None, dano_bonus=0):
        keep_life = alvo.status_atual['PV']
        if len(dano) > 1:
            dano = Combate.danoAleatorio(dano)
        dano += dano_bonus
        dano -= alvo.status['RDF']
        if dano > 0:
            match tipo:
                case 'cortante':
                    Combate.danoGeral(alvo, dano)
                case 'perfurante':
                    if alvo.status_atual['PA'] > 0:
                        Combate.danoGeral(alvo, ceil(dano / 2))
                        alvo.status_atual['PV'] -= floor(dano / 2)
                    else:
                        alvo.status_atual['PV'] -= dano
                case 'concussão':
                    alvo.status_atual['PV'] -= dano
            Hud.msgDano(alvo.info["nome"], dano, tipo)
        else:
            Hud.msgDano(alvo.info["nome"], 0)

    @staticmethod
    def danoMagico(alvo, dano: list, tipo: str, dano_bonus=0):
        # Causar dano aleatório se o dano for maior que 1
        if len(dano) > 1:
            dano = Combate.danoAleatorio(dano)
        else:
            dano = dano[0]
        dano += dano_bonus
        dano -= alvo.status['RDM']
        if dano > 0:
            # ============= Tipos de Dano Mágico ================
            match tipo:
                # Dobro de dano nos PVs
                case 'ácido':
                    if alvo.status_atual['PA'] <= 0:
                        alvo.status_atual['PV'] -= 2 * dano
                    else:
                        alvo.status_atual['PA'] -= dano
                        dano_excedente = alvo.status_atual['PA']
                        if alvo.status_atual['PA'] <= 0:
                            alvo.status_atual['PA'] = 0
                            alvo.status_atual['PV'] += dano_excedente
                case _:
                    Combate.danoGeral(alvo, dano)
            # Mostras mensagem de dano
            Hud.msgDano(alvo.info["nome"], dano, tipo)

    @staticmethod
    def danoAleatorio(dano: list):
        dano_final = randint(dano[0], dano[1])
        return dano_final
