#!/usr/bin/env python3
n = int(input())
t,a = map(int,input().split())
h_n = list(map(int,input().split()))
now,ans = float('inf'),-1
for i in range(n) :
    t_i = abs(1000*a-1000*t+6*h_n[i])
    if now > t_i :
        ans = i+1
        now = t_i
print(ans)
