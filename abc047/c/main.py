#!/usr/bin/env python3
s = input()
nowW = True if s[0]== 'W' else False
ans = 0
for i in range(1,len(s)) :
    if (s[i]!='W' and nowW) or (s[i]=='W' and not(nowW)) :
        ans += 1
        nowW = not(nowW)
print(ans)