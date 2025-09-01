#!/usr/bin/env python3
def dfs(x,y,isVertical,stp) :
    global ans
    stack = [(x,y,isVertical,stp)]
    while stack :
        xx,yy,f,stp = stack.pop()
        visited[xx][yy] = True
        if (xx,yy) == goals :
            ans = min(ans,stp)
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)] :
            if f and dy == 0: continue
            if not(f) and dx == 0: continue
            if 0<=dx+xx<h and 0<=dy+yy<w and g[xx+dx][yy+dy] != '#' and not(visited[dx+xx][dy+yy]):
                stack.append((xx+dx,yy+dy,not(f),stp+1))
        # stack.pop()
        # if stp == 100 :
            # print(xx,yy,f,stp)
            # return


h,w = map(int,input().split())
g = [input() for _ in range(h)]
visited = [[False]*w for _ in range(h)]
starts, goals = (0,0), (0,0)
for i in range(h) :
    for j in range(w) :
        if g[i][j] == 'S' : starts = (i,j)
        if g[i][j] == 'G' : goals = (i,j)
ans = float('inf')
dfs(starts[0],starts[1],True,0)
dfs(starts[0],starts[1],False,0)
print(ans if ans != float('inf') else -1)