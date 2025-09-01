#!/usr/bin/env python3
ans = 0
for i in range(12)  :
    s = input()
    ans += 1 if i+1 == len(s) else 0
print(ans)