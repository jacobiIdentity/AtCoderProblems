#!/usr/bin/env python3
# def gcd(a, b):
#     while b: 
#         a, b = b, a % b
#     return a 

import math
from collections import defaultdict
n = int(input())
dots = [list(map(int,input().split())) for _ in range(n)]
d2 = defaultdict(int)
d4 = defaultdict(int)
for i in range(n) :
    for j in range(i+1,n) :
        p1,p2 = (dots[i][0],dots[i][1]),(dots[j][0],dots[j][1])
        if p1[0] > p2[0] :
            p1,p2 = p2,p1
        if p1[0] == p2[0] and p1[1] > p2[1] :
            p1,p2 = p2,p1
        x,y = p2[0]-p1[0],p2[1]-p1[1]
        # xAbs,yAbs = abs(x),abs(y)
        # div = gcd(xAbs,yAbs)
        div = math.gcd(x,y)
        x //= div
        y //= div
        d2[(x,y)] +=1
        d4[(x,y,(p2[0]-p1[0])**2+(p2[1]-p1[1])**2)] +=1
# print(cnt)
# print(d)
# print(d3)
# print(d2)
# print(d4)
# ans = sum([d2[l]*(d2[l]-1)//2 for l in d2])
# # print(ans)
# ans -= sum([d4[l]*(d4[l]-1)//2 for l in d4])//2
# print(ans)
print(sum([d2[l]*(d2[l]-1)//2 for l in d2])-sum([d4[l]*(d4[l]-1)//2 for l in d4])//2)