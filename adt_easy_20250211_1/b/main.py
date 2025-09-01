#!/usr/bin/env python3
n,c = map(int,input().split())
t_n = list(map(int,input().split()))
ans,now = 0,t_n[0]-c
for i in range(n) :
    if t_n[i]-now >= c :
        ans += 1
        now = t_n[i]
print(ans)