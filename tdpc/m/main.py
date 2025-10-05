#!/usr/bin/env python3
from array import array

h,r = map(int,input().split())
MOD =  10**9+7
adj = [list(map(int,input().split())) for _ in range(r)]
m_ij = [[0]*r for _ in range(r)]
for i in range(r) :
    size = (1<<r)*r
    dp =  [0]*size
    # dp = array('I', [0]*size)
    dp[(1<<i)*r + i] = 1
    # dp = [[0]*r for _ in range(1<<r)]
    # dp[1<<i][i] = 1
    for iMask in range(1<<r) :
        if iMask & (1<<i) == 0 :
            continue
        for j in range(r) :
            # if dp[iMask][j] == 0: 
            if dp[iMask*r+j] == 0: 
                continue
            # m_ij[i][j] += dp[iMask][j]
            m_ij[i][j] += dp[iMask*r+j]
            m_ij[i][j] %= MOD
            for k in range(r) :
                if iMask&(1<<k) : continue
                # dp[iMask|(1<<k)][k] += adj[j][k]*dp[iMask][j]
                dp[(iMask|(1<<k))*r+k] += adj[j][k]*dp[iMask*r+j]
    # print(i,end=" ")
    # print(dp)
# print(m_ij)
m_h_ij = [[1 if i==j else 0 for i in range(r)] for j in range(r)]
while h>0 :
    if h%2 :
        new_m_h_ij = [[0]*r for _ in range(r)]
        for i in range(r) :
            for j in range(r) :
                for l in range(r) :
                    new_m_h_ij[i][j] += m_h_ij[i][l]*m_ij[l][j]
                    new_m_h_ij[i][j] %= MOD
        m_h_ij = new_m_h_ij
    h//=2
    new_m_2k_ij = [[0]*r for _ in range(r)]
    for i in range(r) :
        for j in range(r) :
            for l in range(r) :
                new_m_2k_ij[i][j] += m_ij[i][l]*m_ij[l][j]
                new_m_2k_ij[i][j] %= MOD
    m_ij = new_m_2k_ij
print(m_h_ij[0][0]%MOD)
# print(m_h_ij)