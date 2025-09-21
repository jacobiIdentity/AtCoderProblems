#!/usr/bin/env python3
n,m,k = map(int,input().split())
cnt = [0]*n
ans = []
for i in range(k) :
    a,b = map(int,input().split())
    cnt[a-1] += 1
    if cnt[a-1] == m :
        ans.append(a)
print(*ans)