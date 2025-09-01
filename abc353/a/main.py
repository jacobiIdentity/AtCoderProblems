#!/usr/bin/env python3
n = int(input())
h_n = list(map(int, input().split()))
ans = -1
for i in range(n) :
    if h_n[0] < h_n[i] :
         ans = i+1
         break
print(ans)