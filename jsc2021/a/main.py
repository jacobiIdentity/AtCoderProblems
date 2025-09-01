#!/usr/bin/env python3
x,y,z = map(int,input().split())
ans = (y*z)//x
if (y*z)%x == 0 :
    ans -= 1
print(ans)