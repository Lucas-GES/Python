n = input()
arr1 = set(list(map(int, input().split())))
n2 = input()
arr2 = set(list(map(int, input().split())))

arr3 = list(arr1.difference(arr2))

print(len(arr3))
