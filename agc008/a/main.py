#!/usr/bin/env python3
x,y = map(int,input().split())
absX, absY = abs(x),abs(y)
ans = 0
if y == 0 :
    ans = absX
    if x > 0 :
        ans += 1
elif x == 0 :
    ans = absY
    if y < 0 :
        ans += 1
elif absX <= absY :
    ans = absY - absX
    # if 0 < x <= y :
    #     ans += 0
    # elif x < 0 < y :
    #     ans += 1
    # elif y < 0 < x :
    #     ans += 1
    # else :
    #    ans += 1
    if x < 0 :
        ans += 1
    if y < 0 :
        ans += 1
else :
    ans = absX - absY
    if x > 0 :
        ans += 1
    if y > 0 :
        ans += 1
print(ans)
