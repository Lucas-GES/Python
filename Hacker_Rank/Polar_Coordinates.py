import cmath
# Enter your code here. Read input from STDIN. Print output to STDOUT
z = input() # Example: 1+2j

print(*cmath.polar(complex(z)), sep ='\n')
 