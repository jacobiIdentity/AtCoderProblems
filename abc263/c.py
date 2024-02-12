#!/usr/bin/env python3
import sys
n, m = map(int, input().split())
ans = [i for i in range(1,n+1)]
if n == 1 :
    for i in range(m) :
        print(i+1)
    exit()
pos,now = n-2, n-1
while True :
    if ans[0] == m-n+1 :
        print(*ans)
        break
    print(*ans)
    if ans[n-1] < m :
        ans[n-1] += 1
        continue
    for i in range(n-1, -1, -1) :
        if ans[i] < m-n+i+1 :
            tmp = ans[i]
            for j in range(i, n) :
                ans[j] = tmp + j-i +1
            break