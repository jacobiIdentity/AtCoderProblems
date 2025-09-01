#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
now = 0
for i in range(n) :
    if a_n[i] == now+1 :
        # print(i,now,a_n[i])
        now += 1
if now == 0 :
    now = n+1
print(n-now)