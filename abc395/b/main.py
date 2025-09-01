#!/usr/bin/env python3
n = int(input())
ans = [['']*n for _ in range(n)]
for i in range(n) :
    if i <= n-i-1 :
        tmp = '#' if i%2==0 else '.'
        for x in range(i,n-i) :
            for y in range(i,n-i) :
                ans[x][y] = tmp
for i in range(n) :
    print(''.join(ans[i]))