#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
q = int(input())
for i in range(q) :
    query = list(map(int,input().split()))
    if query[0] == 1 :
        a_n[query[1]-1] = query[2]
    else :
        print(a_n[query[1]-1])