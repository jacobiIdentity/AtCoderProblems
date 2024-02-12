#!/usr/bin/env python3
s = input()
ans = ''
for i in range(len(s)) :
    ans += s[i]
    if len(ans) > 2 and ans[-3:] == 'ABC' :
        ans = ans.removesuffix('ABC')
print(ans)