#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
d = dict()
ans = [-1]*n
for i in range(n) :
    if a_n[i] in d :
        ans[i] = d[a_n[i]]
    d[a_n[i]] = i+1
print(*ans)