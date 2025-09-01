#!/usr/bin/env python3
from collections import defaultdict
n,d = map(int,input().split())
a_n = list(map(int,input().split()))
a_n.sort()
candidates = set()
multiplicity = defaultdict(int)
for i in range(n) :
    multiplicity[a_n[i]] += 1
ans = 0
if d==0 :
    for dd in multiplicity :
        if multiplicity[dd]>1:
            ans += multiplicity[dd]-1
    print(ans)
    exit()
for i in range(n) :
    if a_n[i]+d in multiplicity :
        candidates.add((a_n[i],a_n[i]+d))
# print(multiplicity)
# print(candidates)
visited = set()
for bi,bj in sorted(candidates) :
    b1,b2 = bi,bj
    if (b1,b2) in visited :
        continue
    tmp = [multiplicity[b1]]
    while (b1,b2) in candidates :
        visited.add((b1,b2))
        tmp.append(multiplicity[b2])
        b1 += d
        b2 += d
    # print(tmp)
    if len(tmp)== 2:
        ans += min(tmp)
        continue
    c = min(sum(tmp[::2]),sum(tmp[1::2]))
    m = len(tmp)
    dp = [[float('inf')]*2 for _ in range(m+1)]
    for i in range(1,m+1) :
        if i==1 :
            dp[i][0] = 0
            dp[i][1] = tmp[i-1]
            continue
        dp[i][0] = dp[i-1][1]
        dp[i][1] = min(dp[i-1][0],dp[i-1][1])+tmp[i-1]
    c = min(dp[m])
    # stack = []
    # stack.append((0,1,0,True)) #0をx
    # stack.append((0,0,tmp[0],False)) #0をo
    # while stack :
    #     now,oCnt,cost,isO = stack.pop()
    #     if cost > c :
    #         continue
    #     if now == m-1 :
    #         c = min(c,cost)
    #         continue
    #     if not(isO) :
    #         stack.append((now+1,oCnt+1,cost,True))
    #     stack.append((now+1,oCnt,cost+tmp[now+1],False))
    ans += c                    
print(ans)