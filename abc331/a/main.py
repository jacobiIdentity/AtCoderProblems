#!/usr/bin/env python3
M,D = map(int ,input().split())
y,m,d = map(int ,input().split())
if d < D :
    print(y,m,d+1)
else :
    d = 1
    if m < M :
        print(y,m+1,d)
    else :
        print(y+1,1,d)