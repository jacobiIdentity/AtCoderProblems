#!/usr/bin/env python3
from collections import deque,defaultdict
h,w = map(int,input().split())
s_hw = [list(input()) for _ in range(h)]
que = deque()
ans = 0
visited = [[0]*w for _ in range(h)]
for i in range(h) :
    for j in range(w) :
        if s_hw[i][j] == "#" :
            que.append((i,j))
            visited[i][j] = 1
# print(que)
blackCnt = defaultdict(int)
while que :
    candidate = set()
    while que :
        i,j = que.popleft()
        ans += 1
        for dh,dw in [(0,1),(0,-1),(1,0),(-1,0)] :
            if 0<=i+dh<h and 0<=j+dw<w and not visited[i+dh][j+dw] :
                tup = (i+dh,j+dw)
                if blackCnt[tup]>=1 :
                    candidate.discard(tup)
                else :
                    candidate.add(tup)
                blackCnt[tup] += 1
    for i,j in candidate :
        que.append((i,j))
        visited[i][j] = 1
        s_hw[i][j] = "#"
print(ans)