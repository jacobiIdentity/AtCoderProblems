#!/usr/bin/env python3
from collections import defaultdict
n,x = map(int,input().split())
l_n = []
a_nl = []
# a_k = []
for i in range(n) :
    l,*a_i = map(int,input().split())
    l_n.append(l)
    a_nl.append(list(a_i))
    # a_nl.append(defaultdict(int))
    # a_k.append(set())
    # for a in a_i :
    #     if x%a == 0 :
    #         a_nl[i][a] += 1
    #         a_k[i].add(a)
    # a_k[i] = sorted(list(a_k[i]))
    # l_n.append(len(a_k[i]))
# print(l_n)
# print(a_nl)
# print(a_k)
ans = 0
l = 1
for ll in l_n :
    l *= ll
for i in range(l) :
    a,b,c = 1,0,i
    while b < n :
        a *= a_nl[b][c%l_n[b]]
        c //= l_n[b]
        b += 1
    ans += 1 if a==x else 0
print(ans)