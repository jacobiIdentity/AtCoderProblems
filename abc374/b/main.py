#!/usr/bin/env python3
s = input()
t = input()
ans = 0
if s == t :
    print(0)
    exit()
if len(s) < len(t) : ans= len(s)+1
elif len(t) < len(s) : ans= len(t)+1
else : ans = len(s)
for i in range(min(len(s),len(t))) :
    if s[i] != t[i] :
        ans = min(ans, i+1)
print(ans)