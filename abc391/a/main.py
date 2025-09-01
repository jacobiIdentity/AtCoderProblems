#!/usr/bin/env python3
s = input()
ans = ''
for ss in s :
    if ss == 'N' :
        ans += 'S'
    elif ss == 'S' :
        ans += 'N'
    elif ss == 'W' :
        ans += 'E'
    else :
        ans += 'W'
print(ans)