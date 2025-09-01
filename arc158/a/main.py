#!/usr/bin/env python3
t = int(input())
for _ in range(t): 
    abc = sorted(list(map(int,input().split())))
    a,b,c = 0,abc[1]-abc[0],abc[2]-abc[0]
    ans = 0
    if not(a%2==b%2==c%2) :
        ans = -1
    else :
        b //= 2
        c //= 2
        if (2*b-c)%3 != 0 and (2*c-b)%3 != 0 :
            ans = -1
        else :
            ans = float('inf')
            if (2*b-c)%3 == 0 :
                ans = min(ans,b+abs(2*b-c)//3*2)
            if (2*c-b)%3 == 0 :
                ans = min(ans,c-b+abs(2*c-b)//3*2)
    print(ans)