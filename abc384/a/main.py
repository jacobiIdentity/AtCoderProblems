#!/usr/bin/env python3
n,c1,c2 = input().split()
s = input()
ans = ''
for i in range(int(n)) :
    if s[i] == c1 :
        ans += s[i]
    else :
        ans += c2
print(ans)