import math
import logging

logging.basicConfig(level=logging.DEBUG)

# Exercicio 1: Calcular distância euclidiana entre dois pontos.

def calcular_dist_euclidiana(p1, p2):
    """Calcula a distância euclidiana para p1 e p2 em duas dimenções.
    Args:
        p1: lista ou tupla com dois valores, x e y.
        p2: lista ou tupla com dois valores, x e y.

    Return:
        Distância euclidiana de p1 e p2.
    """    
    p1x, p1y = p1
    p2x, p2y = p2

    dx = (p2x - p1x) ** 2
    dy = (p2y - p1y) ** 2
    d = math.sqrt(dx+dy)
    return d

print('Exercicio 1 - distância euclidiana.')

p1, p2 = None, None

while p1 is None or p2 is None:
    raw_p1 = input('Digite os pontos x e y de p1 separados por virgulas: ').strip().split(',')
    raw_p2 = input('Digite os pontos x e y de p2 separados por virgulas: ').strip().split(',')

    try:
        p1 = [int(raw_p1[0]), int(raw_p1[1])]
        p2 = [int(raw_p2[0]), int(raw_p2[1])]
    except Exception as e:
        logging.debug(f'Entrada inválida, com  {e},')

resultado = calcular_dist_euclidiana(p1, p2)
print(f'A distância euclidiana entre os pontos foi de {resultado}.')