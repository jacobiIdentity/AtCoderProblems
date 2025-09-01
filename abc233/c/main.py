#!/usr/bin/env python3
n,x = map(int,input().split())
l_a = [list(map(int,input().split())) for _ in range(n)]
l_a_sort = sorted([(-l_a[i][0],i) for i in range(n)])
pL = 1
for i in range(n) :
    pL *= l_a[i][0]
ans = 0
for i in range(pL) :
    p = 1
    now = i
    for j in range(n) :
        p *= l_a[l_a_sort[j][1]][now%(-l_a_sort[j][0])+1]
        now //= -l_a_sort[j][0]
    
    ans += 1 if p == x else 0
print(ans)

