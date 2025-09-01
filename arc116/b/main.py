#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
a_n.sort()
p = 998244353
acs = [(a_n[i]*pow(2,i,p))%p for i in range(n)]
for i in range(1,n) :
    acs[i] += acs[i-1]
    acs[i] %= p
# print(acs)
ans = sum([pow(a_n[i],2,p) for i in range(n)])%p
# print(ans)
for i in range(n-1) :
    ans += (acs[-1]-acs[i])*a_n[i]*pow(2,p-i-2,p)
    ans %= p
print(ans)