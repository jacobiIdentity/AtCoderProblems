#!/usr/bin/env python3
n,a,b = map(int,input().split())
ans = 0
if n < a :
    ans = 0
elif a <= b : 
    ans = n-a+1 
elif n%a == 0 :
    ans = (n//a-1)*b+1
elif n%a < b :
    ans = (n//a-1)*b+n%a+1
else :
    ans =(n//a)*b
print(ans)