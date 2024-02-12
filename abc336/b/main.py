#!/usr/bin/env python3
n = int(input())
ans = 0
while True :
    if n%2 == 0 :
        n //= 2
        ans += 1
    else :
        break
print(ans)