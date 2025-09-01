#!/usr/bin/env python3
m,d = map(int,input().split())
ans = 0
for i in range(22,d+1) :
    d10,d1 = int(str(i)[0]),int(str(i)[1])
    if d1>=2 and  d10*d1<=m : ans += 1
print(ans)