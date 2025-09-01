#!/usr/bin/env python3
# from collections import deque
# from functools import lru_cache
import sys
# def dfs(x,y,c) :
#     global visited,ans
#     if visited[x][y] : return
#     visited[x][y] = True
#     if c == k :
#         ans += 1
#         # print(x,y)
#         return
#     for di,dj in directions :
#         if 0 <= x+di < h and 0 <= y+dj < w and not(visited[x+di][y+dj]) and s_hw[x+di][y+dj]=='.':
#             dfs(x+di,y+dj,c+1)
# @lru_cache(maxsize=None)
def dfs2(x,y,route) :
    global ans
    if (x,y) in route : return
    tmp = route + ((x,y),)
    if len(tmp) == k+1 :
        ans.add(tmp)
        return
    for di,dj in directions :
        if 0 <= x+di < h and 0 <= y+dj < w and (x+di,y+dj) not in tmp and s_hw[x+di][y+dj]=='.':
            dfs2(x+di,y+dj,tmp)
sys.setrecursionlimit(10**8)
directions = [(1,0),(0,1),(-1,0),(0,-1)]
h,w,k = map(int,input().split())
s_hw = [input() for _ in range(h)]
# print(directions) 
# ans = 0
ans = set()
for i in range(h) :
    for j in range(w) :
        if s_hw[i][j] == '#' : continue
        visited = [[0]*w for _ in range(h)]
        # dfs(i,j,0)
        dfs2(i,j,tuple())
        # cnt = [[0]*w for _ in range(h)]
        # q = deque()
        # q.append((i,j))
        # while q :
        #     vi,vj = q.popleft()
        #     if visited[vi][vj] : continue
        #     visited[vi][vj] = True
        #     if cnt[vi][vj] == k :
        #         ans += 1
        #         continue
        #     for di,dj in directions :
        #         if 0 <= vi+di < h and 0 <= vj+dj < w and not(visited[vi+di][vj+dj]) and s_hw[vi+di][vj+dj]=='.':
        #             q.append((vi+di,vj+dj))
        #             cnt[vi+di][vj+dj] = cnt[vi][vj]+1

# print(ans)
print(len(ans))