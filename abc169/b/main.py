#!/usr/bin/env python3
import math
n = int(input())
ans = 1
l = sorted(list(map(int,input().split())))
for i in range(len(l)):
    ans *= l[i]
    if ans > 10**18 :
        # print(i,l[i],ans)
        ans = -1
        break
print(ans)