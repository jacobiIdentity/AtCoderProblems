#!/usr/bin/env python3
n,d = map(int,input().split())
t_l = [list(map(int,input().split())) for _ in range(n)]
for k in range(1,d+1) :
    ans = 0
    for i in range(n):
        ans = max(t_l[i][0]*(t_l[i][1]+k),ans)
    print(ans)