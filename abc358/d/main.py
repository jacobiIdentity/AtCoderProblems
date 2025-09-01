#!/usr/bin/env python3
import bisect
n,m = map(int,input().split())
a_n = sorted(map(int,input().split()))
b_m = sorted(map(int,input().split()))
used = [0]*n
ans = 0
for b in b_m:
    j = bisect.bisect_left(a_n,b)
    while j < n and used[j]:
        j += 1
    if j < n :
        ans += a_n[j]
        used[j] =True
    else :
        print(-1)
        exit()
print(ans)