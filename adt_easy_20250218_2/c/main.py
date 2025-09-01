#!/usr/bin/env python3
n = int(input())
a_n = [0]+list(map(int,input().split()))
sp = set()
sp.add(0)
now = 0
for i in range(n+1) : 
  now += a_n[i]
  now %= 360
  sp.add(now)
sp.add(360)
sp2 = sorted(list(sp))
ans = 0
for i in range(len(sp)-1) :
  ans = max(ans,sp2[i+1]-sp2[i])
print(ans)
