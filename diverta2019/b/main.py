#!/usr/bin/env python3
r,g,b,n = map(int,input().split())
ans = 0
i = 0
while i*r <= n :
    j = 0
    while i*r + j*g <= n :
        if (n-i*r-j*g)%b==0 :
            ans += 1
        j+=1
    i+=1

print(ans)