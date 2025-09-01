#!/usr/bin/env python3
n = int(input())
h_n = list(map(int,input().split()))
ans = -1 
for i in range(1,n) :
    if h_n[i] > h_n[0] :
        ans = i+1
        break
print(ans)