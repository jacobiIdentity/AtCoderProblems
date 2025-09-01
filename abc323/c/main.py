#!/usr/bin/env python3
import heapq
n,m = map(int,input().split())
a_m = list(map(int,input().split()))
scores = [i+1 for i in range(n)]
top,sec = -1,-1
d = {i:[] for i in range(n)}
for i in range(n) :
    s = input()
    heapq.heapify(d[i])
    for j in range(m) :
        if s[j]=='o' :
            scores[i] += a_m[j]
        else :
            heapq.heappush(d[i],-a_m[j])
    if top == -1 :
        top = scores[i]
    elif top <= scores[i] :
        top,sec = scores[i],top
    elif sec <= scores[i] < top :
        sec = scores[i]
    # print(i,scores[i],d[i],top,sec)
for i in range(n) :
    ans = 0
    score = scores[i]
    if score > sec :
        print(0)
        continue
    while score <= top and d[i]:
        score += -heapq.heappop(d[i])
        ans += 1
    print(ans)

