#!/usr/bin/env python3
n,q = map(int ,input().split())
p_ij = [input() for _ in range(n)]
cms = [[0]*n for _ in range(n)]
for i in range(n) : 
    cnt = 0
    for j in range(n) :
        cnt += 1 if p_ij[i][j] == 'B' else 0
        cms[i][j] = cnt
# print(cms)
all = sum([cms[j][n-1] for j in range(n)])
for  _ in range(q) :
    a,b,c,d = map(int,input().split())
    mid