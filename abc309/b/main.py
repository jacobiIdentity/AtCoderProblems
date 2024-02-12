#!/usr/bin/env python3
n = int(input())
a_ij = [input() for _ in range(n)]
for i in range(n) :
    ans = ''
    for j in range(n) :
        if i == 0 :
            if j == 0 :
                ans += a_ij[1][0]
            else :
                ans += a_ij[0][j-1]
        elif i == n-1 :
            if j == n-1 :
                ans += a_ij[n-2][n-1]
            else :
                ans += a_ij[i][j+1]
        else :
            if j == 0 :
                ans += a_ij[i+1][0]
            elif j == n-1 :
                ans += a_ij[i-1][n-1]
            else :
                ans += a_ij[i][j]
    print(ans)