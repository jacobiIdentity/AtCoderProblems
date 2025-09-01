#!/usr/bin/env python3
n,m = map(int,input().split())
a_b = [tuple(map(int,input().split())) for _ in range(n)]
c_d = []
for i in range(m) :
    c,d = map(int,input().split())
    c_d.append((c,d,i+1))
for i in range(n) :
    a,b = a_b[i][0],a_b[i][1]
    c_d.sort(key=lambda x: (abs(x[0]-a)+abs(x[1]-b),x[2]))
    print(c_d[0][2])