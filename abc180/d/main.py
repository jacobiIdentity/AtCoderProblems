#!/usr/bin/env python3
x,y,a,b = map(int,input().split())
exp = 0
while True :
    if (a-1)*x < b :
        if a*x < y :
            exp += 1
            x *= a
            # print('a',x,exp)
            continue
        else :
            break
    else :
        if x+b >= y :
            break
        else :
            if (y-x)%b == 0 :
                exp -= 1
            exp += (y-x)//b
            x += b*((y-x)//b)
            # print('b',x,exp)
            break
print(exp)
# print(x)