n = list(map(int, input().split()))
nota1 = list(map(float, input().split()))
nota2 = list(map(float, input().split()))
nota3 = list(map(float, input().split()))
result = [nota1] + [nota2] + [nota3]

for i in zip(*result):
    print(sum(i) / len(i))

    

# n, x = map(int, input().split()) 

# sheet = []
# for _ in range(x):
#     sheet.append( map(float, input().split()) ) 

# for i in zip(*sheet): 
#     print( sum(i)/len(i) )