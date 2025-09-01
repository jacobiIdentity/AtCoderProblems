#!/usr/bin/env python3
import itertools
n = int(input())
s_n = []
for _ in range(n) :
    _,*s_i = map(int,input().split())
    s_n.append(set(s_i))
# print(s_n)
ans = 0
for i in range(2,n+1) :
    for perm in itertools.combinations(range(n),i) :
        ps = list(perm) 
        tmp = set(s_n[ps[0]])
        for j in ps :
            tmp &= s_n[j]
        isYes = True
        for k in tmp :
            if k%2==0:
                isYes = False
                break
        if isYes :
            ans += 1
            # print(ps)
            # print(tmp)
            # print(s_n)
print(ans)