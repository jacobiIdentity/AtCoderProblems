#!/usr/bin/env python3
n = int(input())
# ans = set()
ans = 0
k = 1
while k*k <= n :
    if n%k== 0 :
        if k >= n//k-1 :
            break
        ans += n//k-1
    k+=1
print(ans)