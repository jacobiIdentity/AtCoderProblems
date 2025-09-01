#!/usr/bin/env python3
n,x,y = map(int,input().split())
a_n = list(map(int,input().split()))
a_n_x = [a_n[i] for i in range(n) if i%2==0]
a_n_y = [a_n[i] for i in range(n) if i%2==1]
sx = sum(a_n_x)
sy = sum(a_n_y)
xDP = [[0]*(sx*2+1) for _ in range(len(a_n_x)+1)]
yDP = [[0]*(sy*2+1) for _ in range(len(a_n_y)+1)]
# print(a_n_x)
# print(a_n_y)
for i in range(len(a_n_x)+1) :
    if i == 0 :
        xDP[i][sx] = 1
        continue
    for j in range(len(xDP[i])) :
        if i==1 :
            xDP[i][sx+a_n_x[i-1]] = 1
            break
        if 0<=j+a_n_x[i-1]<sx*2+1 :
            xDP[i][j] = max(xDP[i][j], xDP[i-1][j+a_n_x[i-1]])
        if 0<=j-a_n_x[i-1]<sx*2+1 :
            xDP[i][j] = max(xDP[i][j], xDP[i-1][j-a_n_x[i-1]])
for i in range(len(a_n_y)+1) :
    if i == 0 :
        yDP[i][sy] = 1
        continue
    for j in range(len(yDP[i])) :
        if 0<=j+a_n_y[i-1]<sy*2+1 :
            yDP[i][j] = max(yDP[i][j], yDP[i-1][j+a_n_y[i-1]])
        if 0<=j-a_n_y[i-1]<sy*2+1 :
            yDP[i][j] = max(yDP[i][j], yDP[i-1][j-a_n_y[i-1]])

if 0<=x+sx<2*sx+1 and  xDP[len(a_n_x)][x+sx] and 0<=y+sy<sy*2+1 and yDP[len(a_n_y)][y+sy] :
    print('Yes')
else :
    print('No')
