#!/usr/bin/env python3
def distance(x,y,z,w) :
    return (x-z)*(x-z) + (y-w)*(y-w)
n = int(input())
dots = [tuple(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n) :
    for j in range(i+1,n) :
        ans = max(ans,(dots[i][0]-dots[j][0])**2+(dots[i][1]-dots[j][1])**2)
print(ans**0.5)