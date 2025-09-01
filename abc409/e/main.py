#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
x_n = list(map(int,input().split()))
d = defaultdict(set)
for _ in range(n-1) :
    u,v,w = map(int,input().split())
    d[u-1].add((v-1,w))
    d[v-1].add((u-1,w))
stack = []
stack.append((0,-1,0))
ans = 0
while stack :
    now,prev,flg = stack.pop()
    if flg==0 :
        stack.append((now,prev,1))
        for u,w in d[now] :
            if u != prev :
                stack.append((u,now,0))
    else :
        for u,w in d[now] :
            if u != prev :
                ans += w*abs(x_n[u])
                x_n[now] += x_n[u]
print(ans)
