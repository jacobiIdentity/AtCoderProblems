#!/usr/bin/env python3
n = int(input())
a,b = -1,1
b_5 = 5
while b_5 <= n :
    tmp = n - b_5
    stp = 0
    while tmp > 1 :
        if tmp%3 == 0 :
            tmp //= 3
            stp += 1
        else :
            break
    if tmp == 1 :
        a=stp
        break
    b_5 *= 5
    b += 1
if a < 1 :
    print(-1)
else :
    print(a,b)
        
