#!/usr/bin/env python3
h,w = map(int,input().split())
a_h = [list(map(int,input().split())) for _ in range(h)]
isYes = True
for i1 in range(h) :
    for i2 in range(i1+1,h) :
        for j1 in range(w) :
            for j2 in range(j1+1,w) :
                if a_h[i1][j1]+a_h[i2][j2] > a_h[i2][j1]+a_h[i1][j2] :
                    isYes = False
                    break
            if not(isYes) : break
        if not(isYes) : break
    if not(isYes) : break
print('YNeos'[not(isYes)::2])