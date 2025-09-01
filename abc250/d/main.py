#!/usr/bin/env python3
import bisect
def eratosthenes2(x):
    if x <= 1 : return []
    is_prime = ([False, True] * (x//2+1))[0: x+1]
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, x+1, 2):
        if not(is_prime[i]):
            continue
        if i*i > x:
            break
        for k in range(i*i, x+1, i):
            is_prime[k] = False
    ret = [i for i in range(x) if is_prime[i]]
    return ret
n = int(input())
t = 1 
while t*t*t < n :
    t+= 1
cs = eratosthenes2(t+1)
ans = 0
for qi in range(1,len(cs)) :
    ans += min(qi,bisect.bisect_right(cs,n//(cs[qi]*cs[qi]*cs[qi])))
# for pi in range(len(cs)-1) :
    # qi = pi+1
    # while qi<len(cs) and cs[pi]*cs[qi]*cs[qi]*cs[qi] <= n :
    #     ans += 1
        # qi +=1
print(ans)