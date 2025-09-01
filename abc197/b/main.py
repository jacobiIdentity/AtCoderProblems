#!/usr/bin/env python3
h,w,x,y = map(int,input().split())
x,y = x-1,y-1
s_h = [input() for _ in range(h)]
ans = 1
for i in reversed(range(x)) :
    if s_h[i][y]=='#' :
        break
    ans += 1
for j in reversed(range(y)) :
    if s_h[x][j]=='#' :
        break
    ans += 1
for i in range(x+1,h) :
    if s_h[i][y]=='#' :
        break
    ans += 1
for j in range(y+1,w) :
    if s_h[x][j]=='#' :
        break
    ans += 1

print(ans)