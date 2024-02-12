#!/usr/bin/env python3
s = input()
max, now = s.count(s[0]), s[0]
for i in range(26) :
    tmp = chr(ord('a')+i)
    cnt = s.count(tmp)
    if max < cnt or (max <= cnt and tmp < now) :
        max = cnt
        now = tmp
print(now)