#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
ans = 0
if a_n == list(range(1,n+1)) : ans = 0
elif a_n == reversed(list(range(1,n+1))) : ans = 1
else :
    ans = min(n-a_n[0]+1,a_n[0]+1)
print(ans)