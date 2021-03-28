arr = set(list(input().split()))
a = int(input())
arr2 = set(list(input().split()))
arr3 = set(list(input().split()))

if arr.issuperset(arr2) and arr.issuperset(arr3):
    print('True')
else:
    print('False')