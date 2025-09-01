#!/usr/bin/env python3
s1,s2 = input().split()
ans = 4
if s1 == s2 == 'sick' : ans = 1
elif s1 == 'sick' and s2 != s1 : ans = 2
elif s2 == 'sick'  : ans = 3
print(ans)
