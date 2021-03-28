n = input()
arr1 = set(list(map(int, input().split())))
n2 = input()
arr2 = set(list(map(int, input().split())))

arr3 = arr1.union(arr2)
arr4 = arr1.intersection(arr2)

print(len(arr3))
print(len(arr4))