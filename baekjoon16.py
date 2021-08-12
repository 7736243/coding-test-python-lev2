import math
import sys

input = sys.stdin.readline

def Prime(num):
    if num==1:    return False
    
    s = int(math.sqrt(num))
    
    for i in range(2, s+1):
        if num%i == 0:    return False
        
    return True

m, n = map(int, input().split())

for i in range(m, n+1):
    if Prime(i):    print(i)