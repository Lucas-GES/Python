from collections import defaultdict

A = defaultdict(list)
B = []

sizeA, sizeB = input().split()

for n in range(int(sizeA)):
    A[input()].append(n+1) 
for n in range(int(sizeB)):
    B = B + [input()]
    
for i in B:
    if i in A:
        print(" ".join(map(str, A[i])))
    else:
        print(-1)
        
# print(A)
# print(B)

           

