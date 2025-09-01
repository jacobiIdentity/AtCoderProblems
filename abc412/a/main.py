#!/usr/bin/env python3
n = int(input())
ans = 0
for _ in range(n) :
    a,b = map(int,input().split())
    ans += 1 if a<b else 0
print(ans)
