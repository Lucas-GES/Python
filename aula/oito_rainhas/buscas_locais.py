from oito_rainhas import NRainhas


def subida_encosta(estado_inicial: NRainhas) -> NRainhas:
    melhor_atual = estado_inicial
    while True:
        adjacentes = melhor_atual.adjacentes()       
        melhor_adjacente = min(adjacentes, key=lambda estado: estado.avaliacao)

        if melhor_adjacente.avaliacao < melhor_atual:
            melhor_atual = melhor_adjacente
        else:
            return melhor_atual