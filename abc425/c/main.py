#!/usr/bin/env python3
n,q = map(int,input().split())
a_n = list(map(int,input().split()))
acs = [0]
for i in range(2*n) :
    acs.append(a_n[i%n]+acs[-1])
# print(acs)
sPos = 0
for _ in range(q) :
    query = list(map(int,input().split()))
    if query[0] == 1 :
        sPos += query[1]
        sPos %= n
    else :
        l,r = sPos+query[1]-1,sPos+query[2]-1
        print(acs[r+1] - acs[l])
