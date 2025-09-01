#!/usr/bin/env python3
n = int(input())
s = [input() for _ in range(n)]
t = [input() for _ in range(n)]
ans = float('inf')
for k in range(4) :
    cost = k
    for i in range(n) :
        for j in range(n) :
            if s[i][j] != t[i][j] :
                cost += 1
    ans = min(ans,cost)
    tmp = [['']*n for _ in range(n)]
    
    for i in range(n) :
        for j in range(n) :
            tmp[i][j] = s[n-1-j][i]
    s = tmp

    ans = min(ans,cost)
print(ans)    