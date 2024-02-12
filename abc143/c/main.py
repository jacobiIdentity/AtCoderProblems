#!/usr/bin/env python3
n = int(input())
s = input()
ans, now, i = 1, s[0], 0
while i < n :
    if now != s[i] :
        ans += 1
        now = s[i]
    i += 1
print(ans)