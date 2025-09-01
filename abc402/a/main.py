#!/usr/bin/env python3
s = input()
ans = ''
for ss in s :
    if not(ss.islower()) :
        ans += ss
print(ans)