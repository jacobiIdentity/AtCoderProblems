#!/usr/bin/env python3
n = int(input())
ps = []
for i in range(n) :
    ps.append((i+1, -input().count('o')))
ps.sort(key=lambda x: (x[1],x[0]))
ans = [x0 for x0, x1 in ps]
print(*ans)    