#!/usr/bin/env python3
n,m = map(int,input().split())
s_n = [input() for _ in range(n)]
ans = max(n,m)
for i in range(2<<n) :
    tastes = [0]*m
    iBiStr = format(i, '#012b')[2:]
    iBiStr = iBiStr[::-1]

    tmp = 0
    for j in range(n) :
        if iBiStr[j] == '1' :
            tmp += 1
            for k in range(m) :
                if s_n[j][k] == 'o' :
                    tastes[k] = 1
    if sum(tastes) == m :
        ans = min(ans, tmp)
print(ans)
