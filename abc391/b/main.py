#!/usr/bin/env python3
n,m = map(int,input().split())
s = [input() for _ in range(n)]
t = [input() for _ in range(m)]
for i in range(n-m+1) :
    for j in range(n-m+1) :
        isYes = True
        if s[i][j] != t[0][0] :
            continue
        for k in range(m) :
            for l in range(m) :
                if s[i+k][j+l] != t[k][l] :
                    isYes = False
                    break
            if not(isYes) :
                break
        if isYes :
            print(i+1,j+1)
            exit()