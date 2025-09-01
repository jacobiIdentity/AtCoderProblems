#!/usr/bin/env python3
n,k = map(int,input().split())
a_n = list(map(int,input().split()))
ans = 1
for i in range(n) :
    ans *= a_n[i]
    if len(str(ans))>k :
        ans = 1
print(ans)