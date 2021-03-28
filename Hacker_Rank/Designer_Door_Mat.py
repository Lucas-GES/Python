enter = input().split()
a = int(enter[0])
b = int(enter[1])

for i in range(1,a,2):    
    print((i * '.|.').center(b, '-'))
print('WELCOME'.center(b, '-'))
for i in reversed(range(1,a,2)):    
    print((i * '.|.').center(b, '-'))
