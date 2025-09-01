#!/usr/bin/env python3
b,c = map(int,input().split())
ans = 0
if b==0 :
    ans = (c+2)//2+(c-1)//2
elif b>0 :
    ans = min(c+1,2*b+1)+max(0,(c-2)//2)+max(0,(c-1)//2)
else :
    ans = max(min(c-2,-2*b-1),0)+(c+1)//2+(c+2)//2
print(ans)