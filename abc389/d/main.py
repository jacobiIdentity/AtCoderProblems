#!/usr/bin/env python3
import math
x = int(input())
l,r = 0,0
ans = 0
# print(-3.4,int(-3.4))
for i in range(-x+1,x+1) :
    tmp = math.sqrt(x**2-(i-1/2)**2)
    tmpL = 1/2-tmp
    tmpR = 1/2+tmp
    # print(i,tmpL,tmpR)
    # print(tmpL,tmpR)
    # if i > -r+1 :
        # ans += min(r,int(tmpR))-max(l,int(tmpL))
    ans += min(r,int(tmpR))-max(l,int(tmpL))
    r = int(tmpR)
    l = int(tmpL)
    # print(l,r)
print(ans)
