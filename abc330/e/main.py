#!/usr/bin/env python3
import copy
n,q = map(int ,input().split())
a_n = list(map(int, input().split()))
frq = {a:a_n.count(a) for a in set(a_n)}
for _ in range(q) :
    i,x = map(int ,input().split())
    if frq[a_n[i-1]] == 1 :
        frq.pop(a_n[i-1])
    else : 
        frq[a_n[i-1]] -= 1
    if x in frq :
        frq[x] += 1
    else :
        frq[x] = 1
        a_n[i-1] = x
    if 0 not in frq :
        print(0)
    else :
        tmp = copy.deepcopy(frq)
        for j in range(10**9) :
            if j not in frq :
                print(j)
                break

