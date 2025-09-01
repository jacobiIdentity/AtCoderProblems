#!/usr/bin/env python3
x = int(input())
ans = (x//11)*2
if 0< x%11 :
    ans += 1
if x%11 > 6 :
    ans += 1
print(ans)
