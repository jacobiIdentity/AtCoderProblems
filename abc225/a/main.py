#!/usr/bin/env python3
s = input()
ans = 0
if s.count(s[0]) == 3 :ans = 1
elif s.count(s[0]) == 2 : ans = 3
elif s.count(s[1]) == 2 : ans = 3
else : ans = 6
print(ans)
