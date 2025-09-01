#!/usr/bin/env python3
n = int(input())
a_ij = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n) :
    if ans >= i :
        ans = a_ij[ans][i]-1
    else :
        ans = a_ij[i][ans]-1
print(ans+1)