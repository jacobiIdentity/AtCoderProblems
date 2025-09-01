#!/usr/bin/env python3
n,m = map(int,input().split())
x_m = list(map(int,input().split()))
a_m = list(map(int,input().split()))
x_a = sorted([(x_m[i]-1,a_m[i]) for i in range(m)])
# print(x_a)
ans,i = 0,0
if x_a[0][0] > 0 :
    print(-1)
    exit() 

while True :
    if i == m-1 :
        dist = n-1-x_a[i][0]
        # print(i,x_a[i],dist)        
        if x_a[i][1] != dist +1 :
            ans = -1
        else :
            ans += dist*(dist+1)//2
        break
    dist = x_a[i+1][0]-x_a[i][0]
    if x_a[i][1] < dist :
        ans = -1
        break
    x_a[i+1] = (x_a[i+1][0],x_a[i+1][1]+x_a[i][1] - dist) 
    # x_a[i+1][1] += x_a[i][1] - dist
    ans += dist*(dist-1)//2 + (x_a[i][1]-dist)*dist
    # print(i,x_a[i],x_a[i+1],dist)
    i += 1
print(ans)