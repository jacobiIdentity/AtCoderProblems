#!/usr/bin/env python3
n = int(input())
ans = []
len = 0
for _ in range(n) :
    c,l = input().split()
    len += int(l)
    if len>100 :
        ans = ["Too Long"]
        continue
    ans.append(c*int(l))
print(''.join(ans))
        