#!/usr/bin/env python3
import sys
n = int(input())
a_n = [0]+list(map(int, input().split()))
ans = []
fst = 0
flg = False
for i in range(1,n+1) :
    visited = [False]*(n+1)
    t = i
    ans = []
    cnt = 0
    while True :
        if t == i and cnt > 1 :
            print(cnt)
            print(*ans)
            exit()
        if visited[t] :
            fst = t
            flg = True
            break
        ans.append(t)
        cnt += 1
        visited[t] = True
        t = a_n[t]
    if flg :
        break
flg = False
ans2 = []
for a in ans :
    if a == fst :
        flg = True
    if flg :
        ans2.append(a)
print(len(ans2))
print(*ans2)