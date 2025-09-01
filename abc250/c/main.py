#!/usr/bin/env python3
n,q = map(int,input().split())
d1 = {i:i for i in range(1,n+1)} #番号⇨位置
d2 = {i:i for i in range(1,n+1)} #位置⇨番号
for _ in range(q) :
    x = int(input())
    if d1[x] == n :
        x = d2[n-1]
    lPos,lVal,rPos,rVal = d1[x],x,d1[x]+1,d2[d1[x]+1]
    d1[lVal],d1[rVal],d2[lPos],d2[rPos] = rPos,lPos,rVal,lVal
    # print(d1)
    # print(d2)
print(*[d2[i] for i in range(1,n+1)])