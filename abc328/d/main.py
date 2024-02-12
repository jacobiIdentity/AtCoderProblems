#!/usr/bin/env python3
s = input()
ans = []
for i in range(len(s)) :
    ans.append(s[i])
    if len(ans) > 2 and "".join(ans[-1:-4:-1]) == 'CBA' :
        for _ in range(3) :
            ans.pop()
print("".join(ans))