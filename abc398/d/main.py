#!/usr/bin/env python3
from collections import defaultdict
n,r,c = map(int,input().split())
s = input()
p,f = (r,c),(0,0)
cloud = {(0,0)}
ans = []
for i in range(n) :
    dir = (1,0)
    if s[i]=='E' :
        dir = (0,-1)
    elif s[i]=='W' :
        dir = (0,1)
    elif s[i]=='S' :
        dir = (-1,0)
    p = (p[0]+dir[0],p[1]+dir[1])
    f = (f[0]+dir[0],f[1]+dir[1])
    cloud.add(f)
    # print(p,f,cloud)
    ans.append('1' if p in cloud else '0')
print(''.join(ans))