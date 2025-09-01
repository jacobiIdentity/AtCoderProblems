#!/usr/bin/env python3
import math
n = int(input())
div = set()
i = 1
while i*i*i<=n :
    if n%i==0 :
        div.add(i)
        # div.add(n//i)
    i += 1
for k in div :
    D = 3*(-k*k + 4*(n//k) )
    if D < 0 : continue
    isSquared = False
    # l = 1
    l = int(math.sqrt(D))
    for i in range(2) :
        if (l+i)*(l+i)== D :
            isSquared = True
            l = l+i
            # break
    if not(isSquared) : continue
    if -3*k+l>=6 and (-3*k+l)%6==0 :
        y = (-3*k+l)//6
        x = y+k
        print(x,y)
        exit()
print(-1)