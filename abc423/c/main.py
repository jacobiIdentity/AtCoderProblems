#!/usr/bin/env python3
n,r = map(int,input().split())
L_i = list(map(int,input().split()))
boundaryPos = -1
ans = 0
for i in range(r) :
    if boundaryPos==-1 and L_i[i]==0 :
        boundaryPos = i
    elif boundaryPos>-1 and L_i[i]==1 :
        ans += 1
if boundaryPos>-1 :
    ans += r-boundaryPos
# print(boundaryPos,r-boundaryPos)
boundaryPos = -1
for i in reversed(range(r,n)) :
    if boundaryPos==-1 and L_i[i]==0 :
        boundaryPos = i
    elif boundaryPos>-1 and L_i[i]==1 :
        ans += 1
# print(boundaryPos,boundaryPos-r+1)
if boundaryPos>-1 :
    ans += boundaryPos-r+1
print(ans)