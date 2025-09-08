#!/usr/bin/env python3
h,w = map(int,input().split())
s_h = [input() for _ in range(h)]
isNo = False
for i in range(h) :
    for j in range(w) :
        cnt = 0
        if s_h[i][j]=="." :
            continue
        if 0<=i+1<h and 0<=j<w and s_h[i+1][j]=="#":
            cnt+=1
        if 0<=i-1<h and 0<=j<w and s_h[i-1][j]=="#":
            cnt+=1
        if 0<=i<h and 0<=j+1<w and s_h[i][j+1]=="#":
            cnt+=1
        if 0<=i<h and 0<=j-1<w and s_h[i][j-1]=="#":
            cnt+=1
        if not(cnt == 2 or cnt == 4) :
            isNo = True
            print("No")
            exit()
print("YNeos"[isNo::2])
