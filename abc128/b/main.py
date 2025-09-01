#!/usr/bin/env python3
n = int(input())
ans = []
for i in range(n) :
    s,p = input().split()
    ans.append((s,-int(p),i+1))
ans.sort()
for i in range(n) :
    print(ans[i][2])