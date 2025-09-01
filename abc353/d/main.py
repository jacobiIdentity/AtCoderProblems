#!/usr/bin/env python3
n = int(input())
a_n = list(map(int, input().split()))
ans = 0
for j in range(n) :
    ans += j*a_n[j]
    ans %= 998244353
digits = [[0]*n for _ in range(11)]
for i in reversed(range(1,n)) :
    for k in range(11) :
        if i < n-1 :
            digits[k][i] = digits[k][i+1]
        if k == len(str(a_n[i])):
            digits[k][i] += 1
for i in range(n-1) :
    for k in range(11) :
        ans += a_n[i]*(10**k)*digits[k][i+1]
        ans %= 998244353
print(ans)
