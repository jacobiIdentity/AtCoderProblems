#!/usr/bin/env python3
n,k = map(int,input().split())
a_k = [1]*k
# print(a_k)
for i in range(k,n+1) :
    if i==k :
        a_k.append(k%(10**9))
    else :
        a_k.append((a_k[-1]*2- a_k[i-k-1])%(10**9))
    # a_k.append((a_k[-1]*2- a_k[i-k])%(10**9))
# print(a_k)
print(a_k[-1])