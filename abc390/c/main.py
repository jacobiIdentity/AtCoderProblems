#!/usr/bin/env python3
h,w = map(int,input().split())
s_h = [input() for _ in range(h)]
h0,h1,w0,w1 = -1,-1,w,-1
for i in range(h) :
    for j in range(w) :
        if s_h[i][j] == '#' :
            if h0 == -1 :
                h0 = i
            h1 = max(i,h1)
            w0 = min(w0,j)
            w1 = max(w1,j)
isYes = True
# print(h0,h1,w0,w1)
for i in range(h) :
    for j in range(w) :
        if s_h[i][j] == '.' and h0<=i<=h1 and w0<=j<=w1 : 
            isYes =False
            break
    if not(isYes) :
        break
print('YNeos'[not(isYes)::2])
