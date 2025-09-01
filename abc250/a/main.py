#!/usr/bin/env python3
h,w = map(int,input().split())
r,c = map(int,input().split())
ans = 0
if 1<=r+1<h+1 : ans += 1
if 1<=r-1<h+1 : ans += 1
if 1<=c+1<w+1 : ans += 1
if 1<=c-1<w+1 : ans += 1
print(ans)