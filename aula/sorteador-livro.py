import random
import time

random.seed('Aula IA 18/02/2021')

if __name__ == '__main__':
    with open('nomes-sorteio.txt') as arq:
        nomes = [nome.strip() for nome in arq.readlines() if nome.strip()]
    
    nomes.sort() # Coloca em ordem
    random.shuffle(nomes) # Embaralha a lista

    while len(nomes) > 1:
        eliminado = nomes.pop(0)
        print(f'{eliminado} foi eliminado nesta rodada. Que pena... '
                f'Ainda restam {len(nomes)} postulante.')
        time.sleep(2)

    print(f'O sorteado foi {nomes[-1]}.')
