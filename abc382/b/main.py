#!/usr/bin/env python3
n,d = map(int,input().split())
s = input()
ans = ''
for i in reversed(range(n)) :
    if s[i] == '@' and d>0 :
        ans = '.'+ans
        d -= 1
    else :
        ans = s[i]+ans
print(ans)