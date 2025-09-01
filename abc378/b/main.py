#!/usr/bin/env python3
n = int(input())
q_r = [list(map(int,input().split())) for _ in range(n)]
Q = int(input())
for _ in range(Q) :
    t,d = map(int,input().split())
    q,r = q_r[t-1]
    if r > 0 :
        print(r+q*((d-r-1)//q+1))
    else :
        print(((d-1)//q+1)*q)