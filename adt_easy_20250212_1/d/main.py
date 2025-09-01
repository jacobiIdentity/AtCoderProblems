#!/usr/bin/env python3
n,k = map(int,input().split())
s = input()
ans = ''
tmp = 0
for i in range(n) :
    if s[i] == 'o' and tmp < k :
        ans += 'o'
        tmp += 1
    else :
        ans += 'x'
print(ans)