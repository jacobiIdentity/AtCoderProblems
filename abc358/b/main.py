#!/usr/bin/env python3
n,a = map(int,input().split())
t_n = list(map(int,input().split()))
ans = 0
for i in range(n) :
    if ans <= t_n[i] :
        ans = t_n[i]+a
    else :
        ans += a
    print(ans)
