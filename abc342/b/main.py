#!/usr/bin/env python3
n = int(input())
p_n = list(map(int,input().split()))
order = {p_n[i]:i+1 for i in range(n)}
q = int(input())
for _ in range(q) :
    a,b = map(int,input().split())
    if order[a] < order[b] :
        print(a)
    else :
        print(b)
