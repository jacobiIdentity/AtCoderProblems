#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
d = defaultdict(int)
for _ in range(n) :
    a,b = map(int,input().split())
    d[a] += 1
    d[a+b] -= 1
# print(d)
days = [dd for dd in sorted(d)]
logins = [d[dd] for dd in days]
# print(logins)
for i in range(1,len(logins)) :
    logins[i] += logins[i-1]
# print(days)
# print(logins)
ans = [0]*n
now = days[0]
for i in range(1,len(days)) :
    if logins[i-1] == 0 : continue
    ans[logins[i-1]-1] += days[i]-days[i-1]

print(*ans)