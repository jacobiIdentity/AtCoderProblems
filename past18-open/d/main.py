#!/usr/bin/env python3
n,m = map(int,input().split())
scores = [0]*n
hits = [-1]*n
for _ in range(m) :
    i,*xyz = map(int,input().split())
    if i==1 :
        x,y = xyz[0]-1,xyz[1]-1
        hits[y] = x
        # print(hits)
    else :
        z = xyz[0]-1
        scores[z] -= 1
        if hits[z] > -1 :
            scores[hits[z]] += 1
            hits[z] = -1
        # print(scores)
print(*scores)
