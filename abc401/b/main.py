#!/usr/bin/env python3
n = int(input())
isLogIn = False
ans = 0
for _ in range(n) :
    s = input()
    if s== 'login' :
        isLogIn = True
    elif s=='logout' :
        isLogIn = False
    elif not(isLogIn) and s=='private' :
        ans += 1
print(ans)