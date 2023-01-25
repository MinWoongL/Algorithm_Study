import sys
import math

def n_sum(n):
    nu = 0
    for i in range(1,n+1):
        nu += i
    return nu


T = int(input())

for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    distance = y-x
    
    n = round(math.sqrt(distance))-1
    while 2*n_sum(n) < distance:
        n += 1
    
    if (distance-2*n_sum(n-1)) <= n:
        ans = 2*n-1
    else:
        ans = 2*n
    
    print(ans)
    
    