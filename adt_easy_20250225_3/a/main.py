#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
a1 = a_n[0]
b = set(a_n[1:])
if len(b)== 0 : ans = 0
else :
    aMax = max(b)
    if a1 > aMax : ans = 0
    else : ans = (aMax-a1)+1
print(ans)