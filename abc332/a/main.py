#!/usr/bin/env python3
n,s,k = map(int ,input().split())
p_q =  [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n) :
    ans += p_q[i][0]*p_q[i][1]
print(ans if ans >= s else ans+k)