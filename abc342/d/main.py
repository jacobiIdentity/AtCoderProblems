#!/usr/bin/env python3
from collections import defaultdict
def eratosthenes2(n):
    is_prime = ([False, True] * (n//2+1))[0: n+1]
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, n+1, 2):
        if not(is_prime[i]):
            continue
        if i*i > n:
            break
        for k in range(i*i, n+1, i):
            is_prime[k] = False
    return {p for p in range(n+1) if is_prime[p]}
n = int(input())
a_n = list(map(int, input().split()))
# ps = eratosthenes2(n)
d = defaultdict(int)
for i in range(n) :
    if a_n[i]==0 :
        d[0] += 1
        continue
    j = 2
    while j*j<=a_n[i] :
        if a_n[i]%(j*j)==0 :
            while a_n[i]%(j*j)==0 :
                a_n[i]//= j*j
        j+=1
# for i in range(n) :
#     if a_n[i]==0 :
#         d[0] += 1
#         continue
#     tmp = 1
#     for p in ps :
#         if a_n[i]<p :
#             break
#         if a_n[i]==1 :
#             break
#         if a_n[i]%p==0 :
#             cnt = 0
#             while a_n[i]%p==0 :
#                 cnt += 1
#                 a_n[i]//=p
#             if cnt%2 :
#                 a_n[i]*= p
#                 tmp *= p
#         if a_n[i] == tmp :
#             break
    d[a_n[i]] += 1
ans = d[0]*(n-d[0])
for i in d :
    ans += (d[i]*(d[i]-1))//2
print(ans)
