#!/usr/bin/env python3
t = int(input())
for _ in range(t) :
    n = int(input())
    ans = 'Same'
    if n%2 != 0 :
        ans = 'Odd'
    if n%4 == 0 :
        ans = 'Even'
    print(ans)