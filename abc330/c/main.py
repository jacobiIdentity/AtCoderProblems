#!/usr/bin/env python3
import math
d = int(input())
x = 0
ans = 2*(10**12)
while x**2 <= 2*(10**12) :
    y= int(math.sqrt(abs(d-x**2)))
    ans = min(ans, abs(x**2+(max(y-1,0))**2-d), abs(x**2+y**2-d), abs(x**2+(y+1)**2-d))
    x+=1
print(ans)