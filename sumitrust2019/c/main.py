#!/usr/bin/env python3
x = int(input())
ans =[0]*(x+1)
ans[0]=1
for i in range(100, x+1) :
    for j in range(100,106) :
        if i-j>-1 and ans[i-j]>0:
            ans[i]=1
print(ans[x])