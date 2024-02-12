import sys
import math
from collections import deque
n, m  = map(int, input().split())
s_n = [input() for _ in range(n)]
f = math.factorial(n)
order = []
for i in range(f) :
    moto = sorted([i for i in range(n)])
    for j in range(n-1, 0, -1) :
        tmp = math.factorial(j)
        order.append(moto.pop(f//tmp))
        moto.sort()
    order += moto
    for k in order :
        

        
