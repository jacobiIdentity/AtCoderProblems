#!/usr/bin/env python3
import sys
def same(x_ij, y_ij) :
    isSame = True
    for i in range(n) :
        for j in range(n) :
            if x_ij[i][j] == 1 and y_ij[i][j] == 0 :
                isSame = False
    return isSame
def rotate(x_ij) :
    tmp = [[0]*n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            tmp[i][j] = x_ij[n-1-j][i]
    return tmp
n = int(input())
a_ij = [list(map(int, input().split())) for _ in range(n) ]
b_ij = [list(map(int, input().split())) for _ in range(n) ]
for i in range(3) :
    # print(a_ij)
    if same(a_ij,b_ij) :
        print('Yes')
        exit()
    a_ij = rotate(a_ij)
if same(a_ij,b_ij) :
    print('Yes')
else :
    print('No')
