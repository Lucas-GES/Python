import os
import time
from ambiente import Ambiente
from actions import Actions
import heapq

class Astar():  

    abertos = []
    fechados = []

    def get_jogador():
        return Ambiente.get_jogador 

    def get_ponto():
        return Ambiente.get_ponto 

    def heuristica(p1, p2):
        print(p1,p2)
        x1, y1 = p1
        x2, y2 = p2
        result = abs(x1 - x2) + abs(y1 - y2)        
        return result   

    def verifica_posicao(x, final):
        v = Astar.heuristica(x, final)
        if v not in Astar.fechados:
            a,b = x
            if Actions.valida_movimento(a,b) == True:
                h = Astar.heuristica(x, final)
                heapq.heappush(Astar.abertos, (h, x))
            elif Actions.valida_movimento(a,b) == False:
                h = Astar.heuristica(x, final)
                heapq.heappush(Astar.fechados, (h, x))

    def moverJogador(atual):
        x,y = atual
        for i in range(len(Ambiente.labirinto)):
            for j in range(len(Ambiente.labirinto[0])):
                if Ambiente.labirinto[i][j] == Ambiente.labirinto[x][y]:                    
                    Ambiente.labirinto[i][j] = Ambiente.jogador
                                

    def busca(posicao, abertos, fechados, inicial, final):               
        print(abertos)
        print("entrei")
                    
            
        for i in range(len(Ambiente.labirinto)):
            for j in range(len(Ambiente.labirinto[0])):
                x, y = posicao
                if Ambiente.labirinto[i][j] == Ambiente.labirinto[x][y]:
                        a = i, j-1
                        b = i, j+1
                        c = i-1, j
                        d = i+1, j
                        Astar.verifica_posicao(a, final)
                        Astar.verifica_posicao(b, final)
                        Astar.verifica_posicao(c, final)
                        Astar.verifica_posicao(d, final)
                        x,y = i,j        
                        for i in range(len(Ambiente.labirinto)):
                            for j in range(len(Ambiente.labirinto[0])):
                                if Ambiente.labirinto[i][j] == Ambiente.labirinto[x][y]:
                                    Ambiente.labirinto[i][j] = " "

        os.system('cls||clear') 
        Ambiente.print_labirinto()
        time.sleep(0.5)                        
        valor , mover = abertos[0]                        
        Astar.moverJogador(mover)
        heapq.heappush(fechados, abertos[0])
        heapq.heappop(abertos)

    def main():
        labirinto = Ambiente.labirinto_completo        
        estado_inicial = int(8), int(5)
        f = 0
        for i in range(len(labirinto)):
                for j in range(len(labirinto[0])):
                    if labirinto[i][j] == 'c':
                            x = i
                            y = j
                            posicao_atual = x, y

        for i in range(len(Ambiente.labirinto)):
            for j in range(len(Ambiente.labirinto[0])):
                if Ambiente.labirinto[i][j] == '.':
                    x = i
                    y = j
                    posicao_final = x, y
            
        posicao_atual 
        posicao_final
        Astar.verifica_posicao(estado_inicial, posicao_final) 
        while len(Astar.abertos) > 0:
            
            Astar.busca(posicao_atual, Astar.abertos, Astar.fechados, estado_inicial, posicao_final)
  
        Ambiente.print_labirinto()
        print(Astar.fechados)
        print(Astar.abertos)
    
        
