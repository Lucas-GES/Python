from collections import Counter

print("Number of shoes: ")
n = int(input())
print("The Size of the shoes with space: ")
s = Counter(map(int, input().split()))
print("Number of purchases: ")
x = int(input())
total = []
for i in range(x):
    print(f"Purchase number {i+1}" + ", the number and the price with space: ")
    a,b = map(int, input().split())
    if s[a] > 0:
        total.append(b)
        s.subtract(Counter([a]))

print(f"Total of sells: {sum(total)}$")