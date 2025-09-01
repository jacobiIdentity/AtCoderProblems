#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
a_n.sort()
d = {a_n[i]:min(a_n[i],a_n[-1]-a_n[i]) for i in range(n)}
ans = -1
for i in range(n-1) :
    if d[a_n[i]] > min(ans,a_n[-1]-ans) :
        ans = a_n[i]
print(a_n[-1],ans)