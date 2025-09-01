#!/usr/bin/env python3
from collections import deque
q = int(input())
d = deque()
d.append(1)
ret = 1
for _ in range(q) :
    query = input()
    if query[0]=='1' :
        x = int(query[2:])
        d.append(x)
        ret *=10
        ret += x
        ret %= 998244353
    elif query[0]=='2' :
        x = d.popleft()
        ret -= x*pow(10,len(d),998244353)
        ret %= 998244353
    else :
        print(ret)
