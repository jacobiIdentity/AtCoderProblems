#!/usr/bin/env python3
import bisect
from collections import defaultdict
n,t = map(int, input().split())
s = input()
x_i = list(map(int,input().split()))
d = defaultdict(list)
for i in range(n) :
    d[s[i]].append(x_i[i])
d['0'].sort()
d['1'].sort()
ans = 0
for x in d['1'] :
    left = bisect.bisect_left(d['0'], x)
    right = bisect.bisect_right(d['0'], x+2*t)
    # print(x,left,right)
    ans += right - left
print(ans)