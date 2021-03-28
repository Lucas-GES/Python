n = int(input()) # define a quantidade de numeros a ser digitado
s = set(map(int, input().split())) # digite os numeros dando espaço 

for i in range(int(input())):
    enter = input().split() # digite um dos comandos , de espaço se tiver parametro ex: 'remove 9' 
    comand = enter[0]

    if len(enter) > 1:
        numb = int(enter[1])

    if comand == 'pop':
        s.pop()
    elif comand == 'remove':
        s.remove(numb)
    elif comand == 'discard':
        s.discard(numb)

    print(s)

print(sum(s)) 
 
