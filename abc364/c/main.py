#!/usr/bin/env python3
n,x,y = map(int,input().split())
a_n = sorted(list(map(int,input().split())),reverse=True)
b_n = sorted(list(map(int,input().split())),reverse=True)
ans = float('inf')
tmp = 0
for i in range(n) :
    tmp += a_n[i]
    if tmp > x :
        ans = min(ans,i+1)
tmp = 0
for j in range(n) :
    tmp += b_n[j]
    if tmp > y :
        ans = min(ans,j+1)
if ans == float('inf') :
    ans =n
print(ans)