#!/usr/bin/env python3
n, m = map(int, input().split())
s = input()
t = input()
isP = (s == t[0:n])
isS = (s == t[(m-n):m])
if isP and isS :
    print(0)
elif isP :
    print(1)
elif isS :
    print(2)
else :
    print(3)