#!/usr/bin/env python3
from collections import deque
h,w = map(int,input().split())
a_hw = [input() for _ in range(h)]
que = deque([(0,0,{(0,0)})])
while que :
    x,y,path = que.popleft()
    if (x,y)==(h-1,w-1) :
        isNo = False
        for i in range(h) :
            for j in range(w) :
                if a_hw[i][j]=="#" and (i,j) not in path :
                    isNo = True
                    break
            if isNo :
                break
        # print(path)
        if not(isNo) :
            print('Possible')
            exit()

    for dx,dy in [(0,1),(1,0)] :
        if 0<=x+dx<h and 0<=y+dy<w and a_hw[x+dx][y+dy]=="#" and (x+dx,y+dy) not in path :
            que.append((x+dx,y+dy,path|{(x+dx,y+dy)}))
print('Impossible')