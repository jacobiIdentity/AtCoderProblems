#!/usr/bin/env python3
n,m = map(int,input().split())
a_n = [input() for _ in range(n)]
b_m = [input() for _ in range(m)]
isOK = True
if n==m :
    isOK = True
    for k in range(m) :
        for l in range(m) :
            if a_n[k][l] != b_m[k][l] :
                isOK = False
                break
        if not(isOK ) : break

for i in range(n-m) :
    for j in range(n-m) :
        isOK = True
        for k in range(m) :
            for l in range(m) :
                if a_n[i+k][j+l] != b_m[k][l] :
                    isOK = False
                    break
            if not(isOK ) : break
        if isOK :
            break
    if isOK :
        break
print('YNeos'[not(isOK)::2])


