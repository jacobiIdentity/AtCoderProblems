#!/usr/bin/env python3
n = int(input())
ans = 0
i = 1
while i*i*i < n+1 :
    j = i
    while i*j*j < n+1 :
        ans += n//(i*j)-j+1
        j += 1
    i += 1
print(ans)