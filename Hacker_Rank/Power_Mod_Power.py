a = int(input())
b = int(input())
c = int(input())

result = [pow(a,b)] + [pow(a,b,c)]

print(result[0])
print(result[1])