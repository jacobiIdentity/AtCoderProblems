#!/usr/bin/env python3
n,q = map(int,input().split())
ans = 0
l,r = 0,1
for i in range(q) :
    h,t = input().split()
    t = int(t)-1
    if h == 'L' :
        if l <= t < r \
         or r < l <= t \
         or t <= l < r \
         or r < t <= l :
            ans += abs(l-t)
        elif  t < r < l :
            ans += n-l + t
        elif l < r < t :
            ans += n-t + l
        else :
            print('想定外')
        # print(i,l,r,t)
        l = t
    else :
        if r <= t < l \
         or l < r <= t \
         or t <= r < l \
         or l < t <= r :
            ans += abs(r-t)
        elif  t < l < r :
            ans += n-r + t
        elif r < l < t :
            ans += n-t + r 
        else :
            print('想定外')
        # print(i,l,r,t)
        r = t
print(ans)