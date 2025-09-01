#!/usr/bin/env python3
n,l,r = map(int,input().split())
nStr = format(n,'b')
tmp = 0
ans = 0
for i in reversed(range(len(nStr))) :
    if nStr[i] == '1' :
        tmp = 2**(len(nStr)-i-1)
        tmpMax = tmp*2-1
        ans += max(0,min(tmpMax,r) - max(tmp,l)+1)
print(ans)