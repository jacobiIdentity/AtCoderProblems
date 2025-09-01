#!/usr/bin/env python3
# from collections import defaultdict
n,q = map(int,input().split())
d1 = {i:1 for i in range(1,n+1)}
d2 = {i:i for i in range(1,n+1)}
cnt = 0
for _ in range(q) :
    query = input()
    if  query[0] == '1' :
        _,p,h = map(int,query.split())
        if d1[d2[p]] == 2 :
            cnt -= 1
        d1[d2[p]] -= 1
        d2[p] = h
        d1[h] += 1
        if d1[h] == 2 :
            cnt += 1
    else :
        print(cnt)
    # print(query)
    # print(cnt)
    # print(d1)
    # print(d2)
    # print()