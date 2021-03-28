import math
import os
import random
import re
import sys

def solve(s):
    
    for x in s[:].split(" "): 
        s = s.replace(x, x.capitalize()) 
        s="".join(s) 
    return s

if __name__ == '__main__':
    
    s = input()

    result = solve(s)    
    print(result)