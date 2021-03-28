from __future__ import division

def average(array):
    # your code goes here
    divisor = list(array)
    n = len(set(divisor))   
    divisor = sum(set(divisor))
    result = divisor / n
    return result

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    result = average(arr)
    print (result)