#!/usr/bin/env python3
n = int(input())
s_n = list(map(int,input().split()))
ans = [0]*n
ans[0] = s_n[0]
for i in range(1,n) :
    ans[i] = s_n[i]-s_n[i-1]
print(*ans)

