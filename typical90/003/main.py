#!/usr/bin/env python3
import sys
from collections import deque,defaultdict
sys.setrecursionlimit(10**7)
# def dfs(x,l) :
    # visited[x] = l
def dfs(v) :
    global visited,ans
    if len(graph[v]) == 1 :
        if visited[v] == -1 :
            visited[v] = 1
        p = list(graph[v])[0]
        visited[p] = max(visited[p],visited[n]+1)
        graph[p].discard(v)
        graph[v].discard(p)
        return
    top,second = 1,1
    for y in graph[x] :
        if visited[y] > -1 : continue
        dfs(y,l+1)
        print(x,l,y,visited[y],top,second)
        tmp = visited[y]
        if top <= tmp-l :
            second = top
            top = tmp-l
        elif second < tmp-l :
            second = tmp-l
    print(x,l,top,second)
    ans = max(ans,top+second-1)
    return

n = int(input())
graph = defaultdict(set)
visited = [-1]*n
for _ in range(n-1) :
    a,b = map(int,input().split())
    graph[a-1].add(b-1)
    graph[b-1].add(a-1)
ans = 0
dfs(0,0)
print(ans)
print(visited)