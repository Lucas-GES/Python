n = input()
arr1 = set(list(map(int, input().split())))
n2 = input()
arr2 = set(list(map(int, input().split())))

arr3 = list(arr1.difference(arr2))
arr3 = arr3 + list(arr2.difference(arr1))

print(len(arr3))