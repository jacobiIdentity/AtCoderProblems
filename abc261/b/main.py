#!/usr/bin/env python3
n = int(input())
a_nn = [input() for _ in range(n)]
isY = True
for i in range(n) :
    for j in range(i+1,n) :
        if a_nn[i][j] == 'W' and a_nn[j][i] == 'W' :
            isY = False
        if a_nn[i][j] == 'L' and a_nn[j][i] == 'L' :
            isY = False
        if a_nn[i][j] == 'D' and a_nn[j][i] != 'D' :
            isY = False
        if a_nn[i][j] != 'D' and a_nn[j][i] == 'D' :
            isY = False
print('correct' if isY else 'incorrect')