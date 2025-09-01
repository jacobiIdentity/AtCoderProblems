#!/usr/bin/env python3
s = input()
ans = len(s)
now = 0
for i in reversed(range(len(s))) :
    # print(now,s[i],ans)
    ans += (int(s[i])-now)%10
    now += (int(s[i])-now)%10
print(ans)