#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**9)
cnt = 0
def dfs(x,y,num) :
    global cnt
    if a_hw[x][y] in num :
        return 
    if x == h-1 and y == w-1 :
        cnt += 1
        return
    # print(x,y,cnt,num)
    if x+1 < h :
        dfs(x+1,y, num+[a_hw[x][y]])
    if y+1 < w :
        dfs(x,y+1, num+[a_hw[x][y]])
    
h, w = map(int, input().split())
a_hw = [list(map(int, input().split())) for i in range(h)] 
dfs(0,0,[])
print(cnt)