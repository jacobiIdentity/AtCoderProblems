#!/usr/bin/env python3
n = int(input())
leftPos,rightPos = -1,-1
ans = 0
for _ in range(n) :
    a,s = input().split()
    if s=='L'  :
        if leftPos> -1 :
            ans  += abs(int(a)-leftPos)
        leftPos = int(a)
    else :
        if rightPos> -1 :
            ans  += abs(int(a)-rightPos)
        rightPos = int(a)
print(ans)