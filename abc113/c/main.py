#!/usr/bin/env python3
n,m = map(int,input().split())
p_y = []
for i in range(m) :
    p,y = map(int,input().split())
    p_y.append((p,y,i))
p_y.sort()
ans = ['']*m
now = [0]*(n+1)
for p,y,i in p_y :
    now[p] += 1
    ans[i] =  str(p).zfill(6)+str(now[p]).zfill(6)
print(*ans,sep="\n")