#!/usr/bin/env python3
n = int(input())
t, a = 0, 0
for _ in range(n) :
    tTmp, aTmp = map(int,input().split())
    t += tTmp
    a += aTmp
print('Takahashi' if t > a else 'Aoki' if t < a else 'Draw')