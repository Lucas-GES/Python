import random
from itertools import islice
from typing import Iterable, Optional, List

from oito_rainhas import NRainhas

def subida_encosta(estado_inicial: NRainhas) -> NRainhas:
    melhor_atual = estado_inicial
    while True:
        adjacentes = melhor_atual.adjacentes
        melhor_adjacente = min(adjacentes, key=lambda estado: estado.avaliacao)
        
        if melhor_adjacente.avaliacao < melhor_atual.avaliacao:
            melhor_atual = melhor_adjacente
        else:
            return melhor_atual

def subida_encosta_repetida(gerador: Iterable[NRainhas],
                            repeticoes: Optional[int] = None) -> NRainhas:
    for tentativa, estado_gerado in enumerate(islice(gerador, repeticoes), start=1):
        print(f'Iniciando tentativa {tentativa}...')
        solucao = subida_encosta(estado_gerado)
        if solucao.is_objetivo:
            return solucao


def subida_feixe_local(estados_iniciais: List[NRainhas]) -> NRainhas:
    k = len(estados_iniciais)
    k_atuais = estados_iniciais
    while True:
        k_adjacentes = list()
        for k_atual in k_atuais:
            k_adjacentes += list(k_atual.adjacentes)
        k_adjacentes.sort(key=lambda estado: estado.avaliacao)
        
        if k_adjacentes[0].avaliacao < k_atuais[0].avaliacao:
            k_atuais = k_adjacentes[:k]
        else:
            return k_atuais[0]


def subida_feixe_local_gen(generator: Iterable[NRainhas], k: int) -> NRainhas:
    estados_iniciais = [estado for estado in islice(generator, k)]
    return subida_feixe_local(estados_iniciais)


def busca_genetica(populacao_inicial: List[NRainhas], alfa: float, geracoes: int, objetivo: Optional[int]= None) -> NRainhas:
    assert alfa >=0 and alfa < 1, "Alfa deve estar entre 0 e 1."

    geracao_atual = populacao_inicial
    for count_geracao in range(geracoes):
        # fitness
        fitness_populacao = sum(e.fitness for e in geracao_atual)
        fitnesses_weights = [e.fitness/fitness_populacao for e in geracao_atual]
        print(f'{count_geracao}, '
              f'{fitness_populacao} total fitness, '
              f'{max(e.fitness for e in geracao_atual)} maior fitness, '
              f'{max(geracao_atual, key=lambda e: e.fitness)}')

        if objetivo and max(e.fitness for e in geracao_atual) >= objetivo:
            break

        # selecao
        selecionados = random.choices(geracao_atual, fitnesses_weights, k=len(geracao_atual))

        # crossover
        geracao_atual = []
        for n in range(0, len(selecionados), 2):
            macho, femea = selecionados[n].tabuleiro, selecionados[n+1].tabuleiro
            assert len(macho) == len(femea)

            crosscut = random.randint(1, len(macho)-1)
            geracao_atual.append(NRainhas(tabuleiro=macho[:crosscut] + femea[crosscut:]))
            geracao_atual.append(NRainhas(tabuleiro=femea[:crosscut] + macho[crosscut:]))

        # mutacao
        for individuo in geracao_atual:
            individuo.tabuleiro = [gene if random.random() > alfa else random.randint(0,7)
                                   for gene in individuo.tabuleiro]
    
    # print(geracao_atual)
    return max(geracao_atual, key=lambda i: i.fitness)
