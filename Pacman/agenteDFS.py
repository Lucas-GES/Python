from ambiente import Ambiente
from actions import Actions
import random
import os

class AgenteDFS():

    # labirinto = Ambiente.get_labirinto()

    # def findEnd(moves):      
    #     i = 5
    #     j = 8

    #     for move in moves:
    #         if move == "a":
    #             i -= 1
    #         elif move == "d":
    #             i += 1
    #         elif move == "w":
    #             j -= 1
    #         elif move == "s":
    #             j += 1
    #     if AgenteDFS.labirinto[j][i] == ".":            
    #         AgenteDFS.movimentos = list(moves)                        
    #         return True

    #     return False

    # def achar_final():
    #         visited = []
    #         movimentos = []
    #         add = ""
    #     while not AgenteBFS.findEnd(add):
    #         for i in movimentos:
    #             add += i
    #         if visited is None:
    #             visited = set()
    #         visited.add(add)
    #         for next in graph[start] - visited:
    #             achar_final(graph, next, visited)
    #         return visited
        
    def exec():
        start = Ambiente.get_jogador()
        end = Ambiente.get_ponto()
        AgenteDFS.achar_final(AgenteDFS.labirinto, start )

