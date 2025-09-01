#!/usr/bin/env python3
from collections import defaultdict
n,m = map(int,input().split())
# gridtToC = dict()
grid =defaultdict(list)
for _ in range(m):
    x,y,c = input().split()
    x,y = int(x)-1,int(y)-1
#     gridtToC[(x,y)] = c
    grid[x].append((y,c))
isNo = False
for x in grid :
    grid[x].sort()
lastBpos = n
for i in sorted(grid) :
    leftPosW,rightPosB = n,-1
    for j,c in grid[i] :
        if c == "B" :
            rightPosB = max(rightPosB,j)
        else :
            leftPosW  = min(leftPosW,j)
    if leftPosW == n :
        if lastBpos < rightPosB :
            isNo = True
            break
        lastBpos = min(lastBpos,rightPosB,leftPosW-1)
    elif rightPosB== -1 :
        lastBpos = min(lastBpos,leftPosW-1)
    else :
        if lastBpos < rightPosB :
            print(i,lastBpos,rightPosB,leftPosW)
            isNo = True
            break
        if leftPosW <= rightPosB :
            print(i,lastBpos,rightPosB,leftPosW)
            isNo = True
            break
        lastBpos = min(lastBpos,rightPosB,leftPosW-1)
print('YNeos'[isNo::2])


# sortedGridToC = sorted(list(gridtToC.keys()))
# bMax,bMaxPos,nowColor = n,-1,gridtToC[sortedGridToC[0]]
# for x,y in sortedGridToC :


#     if gridtToC[(x,y)] == 'B' :
#         if bMax >= y :
#             if bMaxPos== x and nowColor == 'B' :
#                 continue
#             else :
#                 bMax,bMaxPos,nowColor = y,x,'B'
#         else :
#             ans = 'No'
#             break
#     else :
#         if bMaxPos != x :
#             bMax,bMaxPos,nowColor = min(y-1,bMax),x,'W'
#         elif nowColor == 'W' :
#             bMax = y-1
#         else :
#             ans = 'No'
#             break
# print(ans)

