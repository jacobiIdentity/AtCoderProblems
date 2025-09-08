#!/usr/bin/env python3
n = int(input())
a_ij = [list(map(int,input().split())) for _ in range(n)]

cost = [[float("inf")]*n for _ in range(1<<n)]
cost[1][0] = 0
for vSet in range(1<<n) :
    for lastV in range(n) :
        if cost[vSet][lastV] == float("inf") :
            continue
        for u in range(n) :
            if vSet & (1<<u) :
                continue
            cost[vSet|(1<<u)][u] = min(cost[vSet][lastV] +a_ij[lastV][u],cost[vSet|1<<u][u])
# print(min(cost[-1]))
# print(cost)
ans = float('inf')
for i in range(1,n) :
    ans = min(cost[-1][i]+a_ij[i][0],ans)
print(ans)
