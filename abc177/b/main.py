#!/usr/bin/env python3
s = input()
t = input()
ans = len(t)
for i in range(len(s)-len(t)+1) :
    tmp = 0
    for j in range(len(t)) :
        tmp += 1 if t[j] != s[i+j] else 0
    ans = min(ans,tmp)
print(ans)


