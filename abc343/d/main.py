#!/usr/bin/env python3
from collections import defaultdict
n,t = map(int,input().split())
ans = 1
scores = [0]*n
dScores = defaultdict(int)
dScores[0] = n
for _ in range(t) :
    a,b = map(int,input().split())
    dScores[scores[a-1]]   -= 1
    if dScores[scores[a-1]] == 0 :
        ans -= 1
    scores[a-1] += b
    dScores[scores[a-1]] += 1
    if dScores[scores[a-1]] == 1 :
        ans += 1
    print(ans)
