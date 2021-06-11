# 1ª geração
[
    NRainhas(tabuleiro=[7, 0, 5, 1, 6, 6, 2, 3]), # 24 - 0.2926829268292683
    NRainhas(tabuleiro=[0, 3, 1, 1, 3, 1, 5, 6]), # 17 - 0.2073170731707317
    NRainhas(tabuleiro=[2, 0, 6, 4, 3, 2, 6, 5]), # 21 - 0.25609756097560976
    NRainhas(tabuleiro=[0, 5, 5, 4, 2, 1, 4, 1]), # 20 - 0.24390243902439024
]

# 2ª geração
[
    NRainhas(tabuleiro=[2, 0, 1, 4, 6, 6, 2, 2]), # 21 - 0.2625
    NRainhas(tabuleiro=[7, 0, 5, 1, 3, 2, 6, 5]), # 18 - 0.225
    NRainhas(tabuleiro=[7, 0, 5, 1, 6, 2, 5, 6]), # 20 - 0.25
    NRainhas(tabuleiro=[0, 3, 1, 1, 6, 6, 2, 3]), # 21 - 0.2625
]

# 3ª geração
[
    NRainhas(tabuleiro=[2, 0, 1, 4, 6, 6, 2, 5]), # 23 - 0.27710843373493976
    NRainhas(tabuleiro=[7, 0, 5, 1, 3, 2, 6, 2]), # 20 - 0.24096385542168675
    NRainhas(tabuleiro=[7, 0, 5, 1, 3, 2, 6, 6]), # 18 - 0.21686746987951808
    NRainhas(tabuleiro=[7, 0, 5, 1, 6, 2, 0, 5]), # 22 - 0.26506024096385544
]

# 4ª geração
[
    NRainhas(tabuleiro=[7, 0, 5, 1, 6, 2, 0, 5]), # 22
    NRainhas(tabuleiro=[7, 0, 5, 1, 3, 2, 6, 6]), # 18
    NRainhas(tabuleiro=[7, 0, 5, 7, 3, 2, 6, 6]), # 17
    NRainhas(tabuleiro=[7, 0, 5, 1, 3, 2, 6, 2]), # 20
]

""" 
sum([ , , , ])
[n/result for n in [ , , , ]]
import random
random.random()

random.randint(1,7)
    alpha = .05
    [(n, random.randint(0,7)) for n in range(32) if random.random() <  alpha]

[n.fitness for n in [
NRainhas(tabuleiro=[7, 0, 5, 1, 6, 2, 0, 5]),
NRainhas(tabuleiro=[7, 0, 5, 1, 3, 2, 6, 6]),
NRainhas(tabuleiro=[7, 0, 5, 7, 3, 2, 6, 6]),
NRainhas(tabuleiro=[7, 0, 5, 1, 3, 2, 6, 2]),
]]