#!/usr/bin/env python3
k = int(input())
s = list(input())
t = list(input())
ds = {i:0 for i in range(1,10)}
dt = {i:0 for i in range(1,10)}
dAll = {i:0 for i in range(1,10)}
for i in range(4) :
    ds[int(s[i])] += 1
    dt[int(t[i])] += 1
    dAll[int(s[i])] += 1
    dAll[int(t[i])] += 1
ans = 0
# print(ds)
# print(dt)
# print(dAll)
for i in range(1,10) :
    for j in range(1,10) :
        if i==j :
            p = (k-dAll[i])*(k-dAll[i]-1)
        else :
            p = (k-dAll[i])*(k-dAll[j])
        if p==0 :
            continue
        ds[i] += 1
        dt[j] += 1
        diff = 0
        for l in range(1,10) :
            diff += l*((10**ds[l]) - (10**dt[l] ))
        # print(i,j,p,diff)
        if diff>0 :
            # print(i,j,diff,p)
            ans+=p
        ds[i] -= 1
        dt[j] -= 1
print(ans/((9*k-8)*(9*k-9)))