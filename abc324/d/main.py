#!/usr/bin/env python3
n = int(input())
s = input()
sTuple = tuple(sorted(list(str(s))))
ans = 0
tmp = 0
while tmp*tmp < 10**n :
    sq = tmp*tmp
    if sTuple == tuple(sorted(list(str(sq))+['0']*(n-len(str(sq))))) :
        ans += 1
    tmp += 1
print(ans)