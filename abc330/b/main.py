#!/usr/bin/env python3
n,l,r = map(int, input().split())
a_n = list(map(int, input().split()))
ans = []
for a in a_n :
    if a < l :
        ans.append(l)
    elif a > r :
        ans.append(r)
    else :
        ans.append(a)
print(*ans)