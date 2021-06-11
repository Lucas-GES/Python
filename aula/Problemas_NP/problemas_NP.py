# 1. Escreva um algoritmo em Python que decida se é 
# possível fazer uma mudança de casa com base nas quantidades
#  que cada caminhão de transporte contratado pode carregar e 
#  no volume dos objetos a serem transportados.
# Assinatura do método a ser implementado: 
# `def eh_possivel_transportar(objetos: Iterable[int], transportes: Iterable[int]) -> bool`

# Por exemplo, se você precisa transportar 5 objetos com volumes 4, 5, 2, 2, 2 
# e dispõe de três carretas com capacidades 3, 8 e 5, você faz uma chamada ao método 
# `eh_possível_transportar((4, 5, 2, 2, 2), (3, 8, 5))`.
n1 , n2 = [] , []
def eh_possivel_transportar(objetos:[int], transportes: [int]) -> bool:
    n = 0
    index = 0
    for i in objetos:
                
        for j in range(len(transportes)):            
            if i <= transportes[j]:                
                print(objetos, transportes, end='\n')
                n = transportes[j] - i
                del(objetos[index])                    
                transportes.remove(transportes[j])
                transportes.insert(j, n)                    
                j = 0         
            elif i > transportes[j]:
                print("É maior, passa reto!!!")
            print(objetos, transportes, end='\n')       

n1 , n2 = list(map(int, input().split())), list(map(int, input().split()))

eh_possivel_transportar(n1, n2)