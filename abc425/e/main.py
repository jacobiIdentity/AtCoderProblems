#!/usr/bin/env python3
t,m = map(int,input().split())
factorial = [1]*5001
for i in range(5000) :
    factorial[i+1] = (factorial[i]*(i+1))
binom = [[0]*(i+1) for i in range(5001)]
binom[0][0] = 1
for i in range(1,5001):
    binom[i][0] = 1
    binom[i][i] = 1
    for j in range(1,i) :
        binom[i][j] = (binom[i-1][j-1]+binom[i-1][j])%m
for _ in range(t) :
    n = int(input())
    c_n = list(map(int,input().split()))
    ans = 1
    now = 0
    for i in range(n) :
        now += c_n[i]
        ans *= binom[now][c_n[i]]
        ans %= m
    print(ans%m)
