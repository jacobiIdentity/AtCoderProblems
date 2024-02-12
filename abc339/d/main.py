#!/usr/bin/env python3
n = int(input())
a_n = list(map(int, input().split())) 
ans = 0
for i in range(n) :
    ans += a_n[i]
    ans = max(ans, 0)
print(ans)
