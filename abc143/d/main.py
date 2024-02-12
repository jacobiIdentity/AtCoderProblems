#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
l_n = list(map(int, input().split()))
d = defaultdict(int)
for l in l_n :
    d[l] += 1
# print(d)
acc = [0]*2001
for i in range(1,2001) :
    acc[i] += d[i] + acc[i-1]
ans = 0
for i in range(n) :
    for j in range(i+1,n) :
        ans += acc[l_n[j]+l_n[i]-1] - acc[abs(l_n[i]-l_n[j])]
        if abs(l_n[i]-l_n[j]) < l_n[i] :
            ans -= 1
        if abs(l_n[i]-l_n[j]) < l_n[j] :
            ans -= 1
print(ans//3)