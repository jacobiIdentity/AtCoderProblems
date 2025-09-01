#!/usr/bin/env python3
import itertools
n,m = map(int,input().split())
a_n =list( map(int,input().split()))
acs = list(itertools.accumulate([0]+a_n))
tmp = sum([(i+1)*a_n[i] for i in range(m)])
ans = tmp
for i in range(1,n-m+1) :
    # print(i,m*a_n[m+i-1],acs[i+m-1]-acs[i-1],tmp,tmp+m*a_n[m+i-1]-acs[i+m-1]+acs[i-1])
    tmp += m*a_n[m+i-1]-acs[i+m-1]+acs[i-1]
    ans = max(ans,tmp)
print(ans)