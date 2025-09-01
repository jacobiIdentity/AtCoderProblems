#!/usr/bin/env python3
n = int(input())
ans = n
if int(str(n)[0]*3) < n :
    ans = str(n//100+1)*3
else :    
    ans = str(n//100)*3
print(ans)