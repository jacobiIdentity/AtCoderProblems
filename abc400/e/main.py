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
    ret = [i for i in range(1,n+1) if is_prime[i]]
    # return is_prime
    return ret
    
ps = eratosthenes2(1000000)
# print(ps)
num400s = []
for i in range(len(ps)-1) :
    a1 = 2
    p1 = ps[i]
    while (p1**a1)*(p1**2) <= 10**12 :
        a2 = 2
        while  (p1**a1)*(ps[i+1]**a2) <= 10**12 :
            ok,ng = i+1,len(ps)
            tmp = p1**a1
            while ng-ok > 1 :
                mid = (ok+ng)//2
                if tmp*(ps[mid]**a2) <= 10**12 :
                    ok = mid
                else :
                    ng = mid
            for j in range(i+1,ok+1) :
                num400s.append(tmp*(ps[j]**a2))
            a2 += 2
        a1 += 2
num400s.sort()
# print(len(num400s))
# print(num400s)
q = int(input())
for _ in range(q) :
    a = int(input())
    pos = bisect.bisect_right(num400s,a)
    print(num400s[pos-1])