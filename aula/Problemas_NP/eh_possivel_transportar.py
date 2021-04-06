def eh_possivel_transportar(objetos:[int], transportes: [int]) -> bool:
        
    for i in range(len(objetos)):                
        if len(objetos) > 0:
            i = 0            
            for j in range(len(transportes)):
                if len(transportes) > 0:
                    j = 0
                    if objetos[i] >= transportes[j]:                        
                        objetos[i] = objetos[i] - transportes[j]
                        del(transportes[j])                        
                    elif objetos[i] <= transportes[j]:                        
                        transportes[j] = transportes[j] - objetos[i]
                        del(objetos[i])
                                

    if len(objetos) == 0:
        return True
    else:
        return False          

n1 , n2 = [] , []
n1 , n2 = list(map(int, input().split())), list(map(int, input().split()))

print(eh_possivel_transportar(n1, n2))