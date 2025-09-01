#!/usr/bin/env python3
n,m = map(int,input().split())
s_n = [input() for _ in range(n)]
scores = [0]*n
for j in range(m) :
    cnt0 = 0
    for i in range(n) :
        if s_n[i][j]=="0" :
            cnt0 += 1
    if cnt0 == 0 or cnt0 == n :
        continue
    beMinority = True
    if cnt0 > n-cnt0 :
        beMinority = False
    for i in range(n) :
        if beMinority and s_n[i][j] == "0":
            scores[i] += 1
        if not beMinority and not s_n[i][j] == "0":
            scores[i] += 1
# print(scores)
maxScore = max(scores)
ans = []
for i in range(n) :
    if scores[i]==maxScore :
        ans.append(i+1)
print(*ans)