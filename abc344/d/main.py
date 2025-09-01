#!/usr/bin/env python3
t = input()
n = int(input())
hukuro = [[]]+[input().split() for _ in range(n)]
# dp = [0]*(len(t)+1)+[[0]+[float('inf')]*len(t) for _ in range(n)]
dp = [[0]+[float('inf')]*len(t) for _ in range(n+1)]
for i in range(1,n+1) :
    for j in range(1,len(t)+1) :
        if dp[i-1][j] != float("inf") :
            dp[i][j] = dp[i-1][j]
        for k in range(j) :
            for l in range(1,int(hukuro[i][0])+1) :
                # print(i,j,k,l,t[:k]+hukuro[i][l])
                if t[:j] == t[:k]+hukuro[i][l] :
                    dp[i][j] = min(dp[i][j],dp[i-1][k]+1)
                    # print("if t[:j] == t[:k]+hukuro[i][l] :")
print(dp[n][len(t)] if dp[n][len(t)] != float("inf") else -1)


