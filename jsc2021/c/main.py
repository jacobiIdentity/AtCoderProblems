#!/usr/bin/env python3
a,b = map(int,input().split())
ans= 1
for i in range(1,b) :
    if a%i == 0 and (a//i+1)*i < b+1:
        ans = max(ans,i)
    elif  a%i != 0 and a-1< (a//i+1)*i < b+1 and a-1< (a//i+2)*i < b+1:
        ans = max(ans,i)
print(ans)