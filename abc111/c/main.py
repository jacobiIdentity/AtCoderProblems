#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
v_n = list(map(int,input().split()))
evens = defaultdict(int)
odds = defaultdict(int)
for i in range(n//2) :
    evens[v_n[2*i]] += 1
    odds[v_n[2*i+1]] += 1
e_k = list(evens.keys())
o_k = list(odds.keys())
e_k.sort(key= lambda x: -evens[x])
o_k.sort(key= lambda x: -odds[x])
ans = float('inf')
if o_k[0] != e_k[0] :
    ans = n//2-odds[o_k[0]]+n//2-evens[e_k[0]]
elif len(o_k)==len(e_k)==1 :
    ans = n//2
elif len(o_k)==1 :
    ans = n//2-evens(e_k[1])
elif len(e_k)==1 :
    ans = n//2-odds(o_k[1])
else :
    ans = min(n//2-odds[o_k[0]]+n//2-evens[e_k[1]],n//2-odds[o_k[1]]+n//2-evens[e_k[0]])
print(ans)
