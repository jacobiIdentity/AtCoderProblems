#!/usr/bin/env python3
n = int(input())
d_n_1 = list(map(int,input().split()))
for i in range(n-1) :
    tmp = [0]
    for j in range(i,n-1) :
        tmp.append(tmp[-1]+d_n_1[j])
    print(*tmp[1:])