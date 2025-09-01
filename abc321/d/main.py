#!/usr/bin/env python3
n,m,p = map(int,input().split())
a_n = list(map(int,input().split()))
b_m = list(map(int,input().split()))
a_n.sort()
acs = [0]+a_n
for i in range(1,n+1) :
    acs[i] += acs[i-1]
# print(acs)
ans = 0
for i in range(m) :
    if b_m[i]+a_n[-1]<=p :
        ans += acs[-1]
        ans += b_m[i]*n
        continue
    ok,ng = n,-1
    while ok-ng>1 :
        mid = (ok+ng)//2
        if b_m[i]+a_n[mid]> p :
            ok = mid
        else :
            ng = mid
    # print(i,ok,b_m[i],a_n[ok])
    ans += acs[ok]+ b_m[i]*ok + p*(n-ok)
print(ans)
