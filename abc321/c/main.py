#!/usr/bin/env python3
k = int(input())
p_ij = [[0]*10 for _ in range(11)]
p_ij[1] = [1]+[1]*9
for i in range(2,11) :
    for j in range(10) :
        if i-1 <= j :
            for k in range(j) :
                p_ij[i][j] += p_ij[i-1][k]
print(p_ij)
p_ij[1][0] = 0
q_ij = [[0]*10 for _ in range(11)]
for i in range(1,11) :
    for j in range(1,10) :
        if i != 1 and j == 1 :
            q_ij[i][j] = p_ij[i-1][9]
        else :
            q_ij[i][j] += p_ij[i][j-1]
print(q_ij)
