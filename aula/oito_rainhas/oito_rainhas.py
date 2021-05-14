from typing import List
from dataclasses import dataclass

@dataclass
class NRainhas:
    """O tabuleiro é formado por num_rainhas, cada uma em uma
    coluna própria, em sequência. Cada rainha pode assumir 
    num_rainhas posições, que equivalem à linha da coluna em
    que estão posicionadas.
    """
    tabuleiro: List[int]

    @property
    def num_rainhas(self):
        return len(self.tabuleiro)
    
    @property
    def dimensoes(self):
        """Dimensoes 2D do tabuleiro de NRainhas"""
        return self.num_rainhas, self.num_rainhas

    @property
    def is_objetivo(self) -> bool:
        for i, rainha in enumerate(self.tabuleiro):
            restante_tabuleiro = self.tabuleiro[i+1:]
            for j, adjacente in enumerate(restante_tabuleiro, start= i+1):
                if rainha == adjacente:
                    return False
                if rainha + (j - i) == adjacente:
                    return False
                if rainha - (j - i) == adjacente:
                    return False
        
        return True

    @property
    def avaliacao(self) -> int:
        """A função de avaliação nos retorna uma pontuação de qualidade
        do atual estado em relação ao objetivo. O objetivo tem necessariamente
        pontuação zero, e quanto maior, pior a avaliação
        """
        count_duplas_conflito = 0
        for i, rainha in enumerate(self.tabuleiro):
            restante_tabuleiro = self.tabuleiro[i+1:]
            for j, adjacente in enumerate(restante_tabuleiro, start= i+1):
                if rainha == adjacente:
                    count_duplas_conflito += 1
                if rainha + (j - i) == adjacente:
                    count_duplas_conflito += 1
                if rainha - (j - i) == adjacente:
                    count_duplas_conflito += 1

        return count_duplas_conflito 

    @property
    def adjacentes(self) -> List[NRainhas]:
        return pass
        
#Testes unitários de programador preguiçoso
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