#!/usr/bin/env python3
import bisect
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
    return [p for p in range(n+1) if is_prime[p]]
q = int(input())
p1 = set(eratosthenes2(10**5+1))
# p1 = set(eratosthenes2(10**5+1))
ps = [p for p in p1 if (p+1)//2 in p1]
ps.sort()
# print(p1)
# print(ps)
for _ in range(q) :
    l,r = map(int,input().split())
    posL = bisect.bisect_left(ps,l-1)
    posR = bisect.bisect_right(ps,r)
    print(posR-posL)