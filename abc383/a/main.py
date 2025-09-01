#!/usr/bin/env python3
n = int(input())
t_v = [tuple(map(int,input().split())) for i in range(n)]
ans = 0
for i in range(n) :
    if i == 0 :
        ans = t_v[i][1]
        continue
    ans = max(ans - (t_v[i][0]-t_v[i-1][0]),0)+t_v[i][1]
print(ans)