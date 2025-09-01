#!/usr/bin/env python3
n,m = map(int,input().split())
s = [input() for _ in range(n)]
t = [input() for _ in range(m)]
for a in range(1,n-m+2) :
    for b in range(1,n-m+2) :
        isInS = True
        for i in range(m) :
            for j in range(m) :
                if s[a+i-1][b+j-1] != t[i][j] :
                    # print(a,b,i,j,s[a+i-1][b+j-1],t[i][j])
                    isInS = False
                    break
            if not(isInS) : break
        if isInS : 
            print(a,b)
            exit()
print(-1)

