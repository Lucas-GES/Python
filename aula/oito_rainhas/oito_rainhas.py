import random
from dataclasses import dataclass
from typing import List, Tuple, Iterable
from itertools import islice

@dataclass
class NRainhas:
    """O tabuleiro é formado por num_rainhas, cada uma em uma
    coluna própria, em sequência. Cada rainha pode assumir
    num_rainhas posições, que equivalem à linha da coluna em
    que estão posicionadas.
    """
    tabuleiro: List[int]

    @staticmethod
    def max_fitness(num_rainhas) -> int:
        return sum(n for n in range(num_rainhas))

    @staticmethod
    def nrainhas_aleatorios(num_rainhas=8, seed=None) -> Iterable['NRainhas']:
        random.seed(seed)
        while True:
            yield NRainhas([random.randint(0,7) for _ in range(num_rainhas)])
    
    @classmethod
    def create_nrainhas_aleatorios(cls, qtde, num_rainhas=8, seed=None) -> List['NRainhas']:
        return [n for n in islice(cls.nrainhas_aleatorios(num_rainhas, seed), qtde)]

    @property
    def num_rainhas(self) -> int:
        return len(self.tabuleiro)
    
    @property
    def dimensoes(self) -> Tuple[int, int]:
        """Dimensões 2D do tabuleiro de NRainhas"""
        return self.num_rainhas, self.num_rainhas
    
    @property
    def is_objetivo(self) -> bool:
        return not any(True for _ in self.duplas_conflitantes)
    
    @property
    def avaliacao(self) -> int:
        """A função de avaliação nos retorna uma pontuação de qualidade
        do atual estado em relação ao objetivo. O objetivo tem necessariamente
        pontuação zero, e quanto maior, pior a avaliação.
        """        
        return sum(1 for _ in self.duplas_conflitantes)
    
    @property
    def fitness(self) -> int:
        """Fitness é o complemento de avaliação, e vice-versa."""
        return NRainhas.max_fitness(self.num_rainhas) - self.avaliacao
    
    @property
    def duplas_conflitantes(self) -> Iterable[Tuple[int, int]]:
        for i, rainha in enumerate(self.tabuleiro):
            restante_tabuleiro = self.tabuleiro[i+1:]
            for j, adjacente in enumerate(restante_tabuleiro, start=i+1):
                if adjacente in (rainha, rainha + (j-i), rainha - (j-i)):
                    yield i, j
    
    @property
    def adjacentes(self) -> Iterable['NRainhas']:
        for i, coluna in enumerate(self.tabuleiro):
            adjacentes = set(range(self.num_rainhas))
            adjacentes.discard(coluna)
            for adjacente in adjacentes:
                tabuleiro_copiado = list(self.tabuleiro)
                tabuleiro_copiado[i] = adjacente
                yield NRainhas(tabuleiro_copiado)


# Testes unitários de programador preguiçoso
mesma_linha = NRainhas([0]*8)
diagonais = NRainhas(list(range(8)))
diag_inversa = NRainhas(list(range(7,-1,-1)))
solucao1 = NRainhas([0,6,4,7,1,3,5,2])

assert mesma_linha.is_objetivo == False
assert mesma_linha.avaliacao == 28

assert diagonais.is_objetivo == False
assert diagonais.avaliacao == 28

assert diag_inversa.is_objetivo == False
assert diag_inversa.avaliacao == 28

assert solucao1.is_objetivo == True
assert solucao1.avaliacao == 0
