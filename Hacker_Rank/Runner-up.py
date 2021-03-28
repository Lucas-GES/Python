n = int(input())
arr = list(map(int, input().split()))[:n]
arr.sort()
big = arr[-1]
second = 0

for i in range(n-1):
    if arr[i] > second and arr[i] < big :
        second = arr[i]        

if second == 0 :
    for i in range(n-1):
        if arr[i] < second :
            second = arr[i]    
    for i in range(n-1):
        if arr[i] > second and arr[i] < big :
            second = arr[i]

            
print(second)
