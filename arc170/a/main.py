#!/usr/bin/env python3
from collections import defaultdict
# n = int(input())
# s = input()
# t = input()
# dif = []
# d = defaultdict(set)
# for i in range(n) :
#     if s[i] != t[i] :
#         dif.append(i)
#         d[s[i]].add(i)
# ans = 0
# if s==t :
#     ans = 0
# elif (s[dif[0]] == 'A' and s.find('A')>=dif[0]) or (s[dif[-1]] == 'B' and s.rfind('B') <= dif[-1]) :
#     ans = -1
# else :
#     ans = max(len(d['A']),len(d['B']))
# print(ans)
from collections import defaultdict
f = open('myfile.txt', 'w')
f.write('s'+chr(9)+'t'+chr(9)+'ans\n')
n = 5
for ti in range(1<<n) :
    t = ''
    for j in range(n) :
        t =  ('B' if ti & (1<<j) else 'A')+t
    for si in range(1<<n) :
        s = ''
        for k in range(n) :
            s = ('B' if si & (1<<k) else 'A')+s
        # for i in range(n) :
        dif = []
        d = defaultdict(set)
        for i in range(len(s)) :
            if s[i] != t[i] :
                dif.append(i)
                d[s[i]].add(i)
        ans = 0
        if s==t :
            ans = 0
        elif (s[dif[0]] == 'A' and s.find('A')>=dif[0]) or (s[dif[-1]] == 'B' and s.rfind('B') <= dif[-1]) :
            ans = -1
        else :
            ans = max(len(d['A']),len(d['B']))
        f.write((s+chr(9)+t+chr(9)+str(ans))+'\n')
f.close()