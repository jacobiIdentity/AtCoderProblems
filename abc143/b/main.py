#!/usr/bin/env python3
n = int(input())
a_n = list(map(int, input().split()))
ans = 0
for i in range(n) :
    for j in range(i+1,n) :
        ans += a_n[i]*a_n[j]
print(ans)