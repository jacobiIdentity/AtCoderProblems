#!/usr/bin/env python3
from collections import defaultdict
s = input()
t = input().lower()
# d = defaultdict(list)
# for i in range(len(s)) :
#     if s[i] in t :
#         d[s[i]].append(i)
# isYes = False
# if len(d[t[0]]) == 0 or len(d[t[1]]) == 0 or (t[2] != 'x' and len(d[t[2]]) == 0) :
#     print('No')
#     exit()
#     if max(d[t[1]]) < min(d[t[0]]) :
#         print('No')
#     else :
#         print('Yes')
        
import re
if t[2] == 'x' :
    m = re.search(t[0]+'.*'+t[1], s)
else :
    m = re.search(t[0]+'.*'+t[1]+'.*'+t[2], s)
print('Yes' if m is not None else 'No')

# isYes = False
# d = defaultdict(set)
# for ss in s :
#     if ss in t :
#         d[ss].add(s)