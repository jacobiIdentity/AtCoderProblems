#!/usr/bin/env python3
n = int(input())
s_n = [input() for _ in range(n)]
ans = set()
for i in range(n) :
    for j in range(n) :
        if i==j : continue
        ans.add(s_n[i]+s_n[j])
print(len(ans))