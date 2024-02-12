#!/usr/bin/env python3
n =int(input())
a_n = [-1]+list(map(int, input().split()))
called = [False]*(n+1)
for i in range(1,n+1) :
    if not(called[i]) :
        called[a_n[i]] = True
ans = []
for i in range(1, n+1) :
    if not(called[i]) :
        ans.append(i)
print(len(ans))
print(*ans)