#!/usr/bin/env python3
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
    return [i for i in range(n+1) if is_prime[i]]
l,r = map(int,input().split())
ps1 = eratosthenes2(10**7)
# print(ps1)
isOKS = set()
for p in ps1 :
    now = p
    while now <=r :
        if now>= l :
            isOKS.add(now)
        now*= now

is_ok = ([False, True] * ((r-l+1)//2+1))[0: r-l+1+1]
is_ok[1] = False
is_ok[2] = True
for i in range(3, n+1, 2):
    if not(is_ok[i]):
        continue
    if i*i > n:
        break
    for k in range(i*i, n+1, i):
        is_ok[k] = False
return [i for i in range(n+1) if is_ok[i]]
