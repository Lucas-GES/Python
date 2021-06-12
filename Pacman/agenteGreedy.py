from ambiente import Ambiente
from actions import Actions

class AgenteGreddy():
    movimentos = []
    movimento = ""
    labirinto = Ambiente.labirinto_completo

    def heuristica(inicial, final):
        distancia = abs(inicial - final)
        return distancia

