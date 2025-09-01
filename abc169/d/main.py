#!/usr/bin/env python3
n = int(input())
p = 2
ans = 0
while p*p< 10**12 and n>1 :
    if n%p == 0 :
        # print(n,p,ans)
        tmp,div = 0,0
        while n%p == 0 :
            n //= p
            tmp += 1
            if div < tmp :
                div += 1
                tmp = 0
                ans += 1
    p += 1
if n != 1 :
    ans += 1
print(ans)