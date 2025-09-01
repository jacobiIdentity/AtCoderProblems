#!/usr/bin/env python3
n,m = map(int,input().split())
x_k = [set(list(map(int,input().split()))[1:]) for _ in range(m)]
for i in range(1,n+1) :
    for j in range(i+1,n+1) :
        isYes = False
        for xs in x_k :
            if i in xs and j in xs :
                isYes = True
        if not(isYes) : break
    if not(isYes) : break
print('YNeos'[not(isYes)::2]) 
