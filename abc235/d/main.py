#!/usr/bin/env python3
from collections import defaultdict, deque
a,n = map(int,input().split())
d = defaultdict(int)
d[1] = 0
que = deque()
que.append((1,0))
while que :
    x,cnt = que.popleft()
    if x==n :
        break
    if x > 10 and x%10>0 :
        xStr = str(x)
        xRotated = int(xStr[-1]+xStr[:-1])
        if xRotated not in d :
            d[xRotated] = cnt+1
            que.append((xRotated,cnt+1))
    if a*x not in d and len(str(a*x))<= len(str(n)) :
        d[a*x] = cnt+1
        que.append((a*x,cnt+1))
print(-1 if n not in d else d[n])
# print(boards)
# print(d)