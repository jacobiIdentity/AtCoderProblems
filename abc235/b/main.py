#!/usr/bin/env python3
n = int(input())
h_n = list(map(int, input().split()))
ans = 0
for h in h_n :
    if ans < h :
        ans = h
    else :
        break
print(ans)