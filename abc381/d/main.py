#!/usr/bin/env python3
from collections import defaultdict


n = int(input())
a_n = input().split()
ans = 0

double = set()
for i in range(n-1) :
    if a_n[i] == a_n[i+1] :
        double.add(i)

for i in range(n) :
    if i in double :
        used = set()
        used.add(a_n[i])


    
i = 0
while i < n-1 :
    used = set()
    if a_n[i] == a_n[i+1] :
        used.add(a_n[i])
        k = 2
        while i+k+1 < n :
            if a_n[i+k] == a_n[i+k+1] and a_n[i+k] not in used :
                used.add(a_n[i+k])
                k += 2
            else :
                break
        ans = max(ans,k)
        # print(i,k,ans,used)
        i += k-1
    else :
        i += 1

print(ans)