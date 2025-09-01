#!/usr/bin/env python3
n = int(input())
prev = [n+1]+list(map(int,input().split()))
next = {prev[i]:i for i in range(1,n+1)}
ans = []
p = -1
# print(prev)
# print(next)
while p in next :
    ans.append(next[p])
    p = next[p]
print(*ans)
