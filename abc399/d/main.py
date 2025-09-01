#!/usr/bin/env python3
from collections import defaultdict
t = int(input())
for _ in range(t) :
    n = int(input())
    a_n = list(map(int,input().split()))
    d = defaultdict(list)
    for i in range(2*n) :
        d[a_n[i]-1].append(i)
    # print(d)
    ans = set()
    isNg = set()
    for i in range(n) :
        p1,p2 = d[i][0],d[i][1]
        if abs(p2-p1) == 1 :
            isNg.add(i)
    # print(isNg)
    for i in range(n) :
        if i in isNg : continue
        p1,p2 = d[i][0],d[i][1]
        p1Neighbor = set()
        p2Neighbor = set()
        if 0<=p1-1<2*n :
            p1Neighbor.add((a_n[p1-1]-1,p1-1))
        if 0<=p1+1<2*n :
            p1Neighbor.add((a_n[p1+1]-1,p1+1))
        if 0<=p2-1<2*n :
            p2Neighbor.add((a_n[p2-1]-1,p2-1))
        if 0<=p2+1<2*n :
            p2Neighbor.add((a_n[p2+1]-1,p2+1))
        # print(i,p1,p2,p1Neighbor,p2Neighbor)
        for j1,posJ1 in p1Neighbor :
            for j2,posJ2 in p2Neighbor :
                if j1 in isNg : continue
                if j2 in isNg : continue
                if j1==j2 and posJ1 != posJ2 :
                    a,b = i,j1
                    if a>b : a,b = b,a
                    ans.add((a,b))

    print(len(ans))
