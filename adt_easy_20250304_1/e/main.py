#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
def dfs(i,j,nums) :
    global ans
    if a_hw[i][j] in nums :
        return
    if i==h-1 and j== w-1 :
        ans += 1
        return
    tmp = nums + [a_hw[i][j]]
    if 0<=i+1<h :
        dfs(i+1,j,tmp)
    if 0<=j+1<w :
        dfs(i,j+1,tmp)

h,w = map(int,input().split())
a_hw = [list(map(int,input().split())) for _ in range(h)]
ans = 0
dfs(0,0,[])
print(ans)