#!/usr/bin/env python3
n,k = map(int,input().split())
r_n = list(map(int,input().split()))
l = 1
for r in r_n :
    l*= r
for i in range(l) :
    tmp = []
    iTmp = i
    now = n-1
    while now>-1 :
        tmp.insert(0,(iTmp %r_n[now]) + 1)
        iTmp //= r_n[now]
        now -= 1
    if sum(tmp)%k == 0 :
        print(*tmp)
        
