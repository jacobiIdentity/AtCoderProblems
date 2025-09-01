#!/usr/bin/env python3
x = int(input())
ans = 0
for i in range(1,10) :
    for j in range(1,10) :
        if i*j != x :
            ans += i*j
print(ans)