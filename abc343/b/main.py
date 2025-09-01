#!/usr/bin/env python3
n = int(input())
a_ij = [list(map(int, input().split())) for _ in range(n)]
for i in range(n) :
    tmp = []
    for j in range(n) :
        if a_ij[i][j] == 1 :
            tmp.append(j+1)
    print(*tmp)