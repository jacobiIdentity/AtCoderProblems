#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
s = input()
cnts = defaultdict(int)
now = s[0]
cnt = 0
for i in range(n) :
    if s[i] != now :
        cnts[now] = max(cnt, cnts[now])
        now, cnt = s[i],1
    else :
        cnt += 1
    if i == n-1 :
        cnts[now] = max(cnt, cnts[now])
# print(cnts)
print(sum(map(lambda x:cnts[x],cnts)))
    