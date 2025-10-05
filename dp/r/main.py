#!/usr/bin/env python3
MOD = 10**9 + 7
n,k = map(int,input().split())
# a_ij は m^(k)_ij を格納
a_ij = [list(map(int,input().split())) for _ in range(n)]
b_ij = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

while k>0 :
    if k%2 :
        new_b_ij = [[0]*n for _ in range(n)]
        for i in range(n) :
            for j in range(n) :
                for l in range(n) :
                    new_b_ij[i][j] += b_ij[i][l]*a_ij[l][j]
                    new_b_ij[i][j] %= MOD
        b_ij = new_b_ij
    k //= 2
    m_2k_ij = [[0]*n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            for l in range(n) :
                m_2k_ij[i][j] += a_ij[i][l]*a_ij[l][j]
                m_2k_ij[i][j] %= MOD
    a_ij = m_2k_ij
print(sum([sum(b_ij[i])%MOD for i in range(n)])%MOD)