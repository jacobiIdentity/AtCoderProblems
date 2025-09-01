#!/usr/bin/env python3
n,m = map(int,input().split())
a_n = list(map(int,input().split()))
b_m = list(map(int,input().split()))
deletetgt = set()
for i in range(m) :
    for j in range(n) :
        if b_m[i]==a_n[j] and j not in deletetgt :
            deletetgt.add(j)
            break
# print(deletetgt)
print(*[a_n[i] for i in range(n) if i not in deletetgt])