n = input()
arr1 = set(list(map(int, input().split())))
n2 = input()
arr2 = set(list(map(int, input().split())))

arr3 = list(arr1.difference(arr2))
arr3 = arr3 + list(arr2.difference(arr1))

for n in sorted(arr3):
    print(n)

# a,b = [set(raw_input().split()) for _ in range(4)][1::2]
# print '\n'.join(sorted(a^b, key=int))