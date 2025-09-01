#!/usr/bin/env python3
a,b,c = map(int,input().split())
ans = 0
if c == 0 :
    ans = 0
elif c%2!= 0 :
    if a > b :
        ans = 1
    elif a<b :
        ans = -1
else :
    if abs(a) > abs(b) :
        ans = 1
    elif abs(a) < abs(b) :
        ans = -1
print('<' if ans == -1 else ('>' if ans == 1 else '='))
    