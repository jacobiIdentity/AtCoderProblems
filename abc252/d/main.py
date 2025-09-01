#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
a_n = list(map(int,input().split()))
d1 = defaultdict(int)
for i in range(n) :
    d1[a_n[i]] += 1
# print(d1)
if len(d1)<3: 
    print(0)
    exit()

d2Len = defaultdict(int)
for i in d1 :
    d2Len[d1[i]] += 1
# print(d2Len)
d2Keys = list(d2Len.keys())
# d2Keys.sort(key=lambda x:d2Len[x])
ans = 0
already = set()
# print(d2Keys)
for i in range(len(d2Keys)) :
    if d2Len[d2Keys[i]] >= 3 and (i,i,i) not in already:
        ans += d2Keys[i]*d2Keys[i]*d2Keys[i]*((d2Len[d2Keys[i]]*(d2Len[d2Keys[i]]-1)*(d2Len[d2Keys[i]]-2))//6)
        already.add((i,i,i))
    for j in range(i+1,len(d2Keys)) :
        if d2Len[d2Keys[i]] >= 2 and (i,i,j) not in already :
            already.add((i,i,j))
            ans += d2Keys[i]*d2Keys[i]*d2Keys[j]*((d2Len[d2Keys[i]]*(d2Len[d2Keys[i]]-1))//2) *(d2Len[d2Keys[j]])
        if d2Len[d2Keys[j]] >= 2 and (i,j,j) not in already :
            already.add((i,j,j))
            ans += d2Keys[i]*d2Keys[j]*d2Keys[j]*(d2Len[d2Keys[i]])*((d2Len[d2Keys[j]]*(d2Len[d2Keys[j]]-1))//2 )
        for k in range(j+1,len(d2Keys)) :
            if d2Len[d2Keys[i]] >= 2 and (i,i,k) not in already :
                already.add((i,i,k))
                ans += d2Keys[i]*d2Keys[i]*d2Keys[k]*((d2Len[d2Keys[i]]*(d2Len[d2Keys[i]]-1))//2) *(d2Len[d2Keys[k]])
            if d2Len[d2Keys[j]] >= 2 and (j,j,k) not in already :
                already.add((j,j,k))
                ans += d2Keys[j]*d2Keys[j]*d2Keys[k]*((d2Len[d2Keys[j]]*(d2Len[d2Keys[j]]-1))//2) *(d2Len[d2Keys[k]])
            if d2Len[d2Keys[k]] >= 2 and (i,k,k) not in already :
                already.add((i,k,k))
                ans += d2Keys[i]*d2Keys[k]*d2Keys[k]*(d2Len[d2Keys[i]])*((d2Len[d2Keys[k]]*(d2Len[d2Keys[k]]-1))//2)
            if d2Len[d2Keys[k]] >= 2 and (j,k,k) not in already :
                already.add((j,k,k))
                ans += d2Keys[j]*d2Keys[k]*d2Keys[k]*(d2Len[d2Keys[j]])*((d2Len[d2Keys[k]]*(d2Len[d2Keys[k]]-1))//2)
            if  (i,j,k) not in already :
                already.add((i,j,k))
                ans += d2Keys[i]*d2Keys[j]*d2Keys[k]*(d2Len[d2Keys[i]])*(d2Len[d2Keys[j]])*(d2Len[d2Keys[k]])
print(ans)
            

