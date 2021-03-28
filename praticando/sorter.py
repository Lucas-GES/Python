import random
import time

if __name__ == '__main__':
    with open('frases.txt') as arq:
        nomes = [nome.strip() for nome in arq.readlines() if nome.strip()]
    
    nomes.sort() # Coloca em ordem
    random.shuffle(nomes) # Embaralha a lista

    while len(nomes) > 1:
        random.shuffle(nomes)
        frases = nomes[0]
        print(f'{frases}')
        time.sleep(2)

    