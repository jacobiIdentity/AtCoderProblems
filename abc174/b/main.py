#!/usr/bin/env python3
n,d = map(int,input().split())
g = [tuple(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n) :
    if g[i][0]*g[i][0]+g[i][1]*g[i][1]<=d*d :
        ans += 1
print(ans)