#!/usr/bin/env python3
h,w = map(int,input().split())
c = [input() for _ in range(h)]
x_w = [0]*w
for i in range(h) :
    for j in range(w) :
        if c[i][j]=="#" :
            x_w[j] += 1
print(*x_w)
