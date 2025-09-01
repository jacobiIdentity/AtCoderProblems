#!/usr/bin/env python3
n = int(input())
dots = [list(map(int,input().split())) for _ in range(n)]
aveX,aveY = 0,0
minX,minY = float("inf"),float("inf")
maxX,maxY = 0,0
for dot in dots :
    maxX = max(maxX,dot[0])
    maxY = max(maxY,dot[1])
    minX = min(minX,dot[0])
    minY = min(minY,dot[1])
    # aveX += dot[0]
    # aveY += dot[1]
aveX = maxX+minX
aveY = maxY+minY
# print(minX,minY)
# print(maxX,maxY)
# print(aveX,aveY)
# print(aveX//2,aveY//2)
# print(aveX//n,aveY//n)
aveX //= 2
aveY //= 2
ans = 0
for dot in dots :
    ans = max(abs(aveX-dot[0]),abs(aveY-dot[1]),ans)
print(ans)