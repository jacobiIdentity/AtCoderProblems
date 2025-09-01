#!/usr/bin/env python3
import math 
t = int(input())
p = 998244353
for _ in range(t) :
    n,k = map(int,input().split())
    if n == 1 :
        print(1 if k==1 else 0)
        continue
    d = len(bin(n))-2
    if d < k :
        print(0)
        continue
    cnt = 0
    tops = 0
    ans = 0
    for i in reversed(range(d)) :
        if n&(1<<i) :
            # if i==0 and:
            # print(i,cnt,i-1,k-cnt-1,2**i-1,tops,ans)
            if i>0 :
                ans += (math.comb(i-1,k-cnt-1)%p) * ((2**i-1)%p)
                ans %=p
                ans += (math.comb(i,k-cnt)%p) * tops
                ans %=p
            cnt += 1
            tops += 1<<i
            tops %= p
        if cnt==k :
            ans += tops
            ans %=p
            break
    print(ans)