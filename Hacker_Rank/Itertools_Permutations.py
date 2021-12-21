from itertools import permutations

sample = input().split()
word = sample[0]
permutation = int(sample[1])
separeted = []
for n in word:
    separeted += n
    
result = sorted(list(permutations(separeted, permutation)))

for i in result:
    output = ''
    for n in i:
        output += n
    print(output)    
