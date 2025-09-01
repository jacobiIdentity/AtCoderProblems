#!/usr/bin/env python3
n,c = map(int,input().split())
t_n = list(map(int,input().split()))
ans,time = 0,c
for i in range(n) :
    if i > 0 :
        time += (t_n[i]-t_n[i-1])
    if time >= c :
        ans += 1
        time = 0
print(ans)