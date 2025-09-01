#!/usr/bin/env python3
def prime_factorize_set(x) :
    a = set()
    tmp = x
    if x%2 == 0 :
        a.add(2)
        while tmp%2 == 0 :
            tmp //= 2
    div = 3
    while div*div <= x :
        if tmp%div == 0 :
            a.add(div)
            tmp //= div
        else :
            div += 2
    if tmp != 1 :
        a.add(tmp)
    return a

n,m = map(int,input().split())
a_n = list(map(int,input().split()))
ngFactor = set()
for i in range(n) :
    ngFactor |= prime_factorize_set(a_n[i])
ans = {1}
for j in range(1,m+1) :
    if len(prime_factorize_set(j)&ngFactor) == 0 :
        ans.add(j)
print(len(ans))
for aa in sorted(list(ans)) :
    print(aa)
