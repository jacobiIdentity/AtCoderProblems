#!/usr/bin/env python3
from collections import defaultdict
s = input()
d = defaultdict(list)
for i in range(len(s)) :
    d[s[i]].append(i)
ans = 0
for ss in d :
    if len(d[ss]) > 1 :
        l = 0
        r = len(d[ss])
        for i in range(d[ss][-1]) :
            if s[i] == ss :
                ans += l*(r-1)
                l += 1
                r -= 1
            else :
                ans += l*r
        # r = 1
#         while r < len(d[ss]) :
#             ans += (d[ss][r]-d[ss][l]-1)
#             if r < len(d[ss]) - 1 :
#                 r += 1
#             else :
#                 l += 1
#                 r = l+1

print(ans)
